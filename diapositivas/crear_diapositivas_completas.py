import os
import subprocess
import sys
import shutil

def get_conda_env():
    env = os.environ.copy()
    python_dir = os.path.dirname(sys.executable)
    paths_to_add = []
    if os.name == 'nt':
        paths_to_add.append(os.path.join(python_dir, 'Scripts'))
        paths_to_add.append(os.path.join(python_dir, 'Library', 'bin'))
        paths_to_add.append(os.path.join(python_dir, 'Library', 'usr', 'bin'))
        paths_to_add.append(os.path.join(python_dir, 'Library', 'mingw-w64', 'bin'))
    else:
        paths_to_add.append(os.path.join(python_dir, 'bin'))
    for p in paths_to_add:
        if os.path.exists(p):
            env['PATH'] = p + os.pathsep + env['PATH']
    return env
def check_env():
    print("=== VERIFICACIÓN DEL ENTORNO DE DIAPOSITIVAS ===")
    if not os.path.exists("_quarto.yml"):
        print("[ERROR] Este script debe ejecutarse desde la raíz del proyecto.")
        return False
        
    archivos = [
        "diapositivas/portada.qmd",
        "diapositivas/portada.html",
        "diapositivas/tema1_intro.qmd",
        "diapositivas/tema2_opt_no_lineal.qmd",
        "estilos.css"
    ]
    for archivo in archivos:
        if os.path.exists(archivo):
            print(f"[OK] {archivo} encontrado.")
        else:
            print(f"[ERROR] {archivo} NO encontrado.")
            return False
            
    try:
        import pypdf
        print("[OK] pypdf instalado.")
    except ImportError:
        print("[ERROR] pypdf NO instalado. Por favor instálalo en tu entorno de conda.")
        return False
        
    return True

def crear_portada():
    print("1. Generando portada de diapositivas con WeasyPrint...")
    dir_original = os.getcwd()
    os.chdir("diapositivas")
    
    try:
        subprocess.run(["quarto", "render", "portada.qmd", "--to", "pdf", "--quiet"], env=get_conda_env(), check=True)
        if not os.path.exists("portada.pdf"):
            raise FileNotFoundError("portada.pdf no fue generado.")
        print("   [OK] Portada de diapositivas creada.")
    except Exception as e:
        print(f"   [ERROR] Creando portada: {e}")
        raise e
    finally:
        os.chdir(dir_original)

def crear_diapositivas_individuales():
    print("2. Renderizando diapositivas a Beamer PDF...")
    dir_original = os.getcwd()
    os.chdir("diapositivas")
    
    if not os.path.exists("diapositivas_pdf"):
        os.makedirs("diapositivas_pdf")
        
    temas = [
        ("tema1_intro.qmd", "diapositivas_pdf/tema1_intro.pdf", "Tema 1"),
        ("tema2_opt_no_lineal.qmd", "diapositivas_pdf/tema2_opt_no_lineal.pdf", "Tema 2")
    ]
    
    gif_mapping = {
        "busqueda_uniforme.gif": "busqueda_uniforme_concepto.png",
        "dicotomica.gif": "dicotomica_pasos.png",
        "seccion_aurea.gif": "seccion_aurea_pasos.png",
        "biseccion.gif": "biseccion_pasos.png",
        "newton_1d.gif": "newton_1d_pasos.png",
        "coordenadas_ciclicas_ej1.gif": "coordenadas_ciclicas_ej1.png",
        "coordenadas_ciclicas_ej2.gif": "coordenadas_ciclicas_ej2.png",
        "steepest_descent.gif": "steepest_descent_pasos.png"
    }
    
    for qmd, pdf_dest, label in temas:
        print(f"   • Renderizando {label} ({qmd}) a Beamer...")
        
        with open(qmd, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        for gif, png in gif_mapping.items():
            if gif in content:
                content = content.replace(gif, png)
                modified = True
                print(f"     [SUSTITUCIÓN] Reemplazado {gif} por {png}")
                
        qmd_to_render = qmd
        if modified:
            qmd_to_render = "temp_render.qmd"
            with open(qmd_to_render, "w", encoding="utf-8") as f:
                f.write(content)
                
        pdf_tmp = qmd_to_render.replace(".qmd", ".pdf")
        if os.path.exists(pdf_tmp):
            os.remove(pdf_tmp)
            
        try:
            subprocess.run(["quarto", "render", qmd_to_render, "--to", "beamer", "--output", pdf_tmp], env=get_conda_env(), check=True)
            if not os.path.exists(pdf_tmp):
                raise FileNotFoundError(f"{pdf_tmp} no fue generado por Quarto.")
            if os.path.exists(pdf_dest):
                os.remove(pdf_dest)
            shutil.move(pdf_tmp, pdf_dest)
            print(f"     [OK] {label} creado en {pdf_dest}.")
        except Exception as e:
            print(f"     [ERROR] Renderizando {label}: {e}")
            raise e
        finally:
            if modified and os.path.exists(qmd_to_render):
                os.remove(qmd_to_render)
            
    os.chdir(dir_original)

def unir_diapositivas(nombre_salida="DiapositivasOptimizacionAnalisisRedes.pdf"):
    print("3. Uniendo PDFs de diapositivas...")
    dir_original = os.getcwd()
    os.chdir("diapositivas")
    
    portada_path = "portada.pdf"
    output_dir = "diapositivas_pdf"
    final_pdf_path = os.path.join(output_dir, nombre_salida)
    
    temas = [
        ("diapositivas_pdf/tema1_intro.pdf", "Tema 1: Introducción a la Investigación Operativa"),
        ("diapositivas_pdf/tema2_opt_no_lineal.pdf", "Tema 2: Optimización No Lineal")
    ]
    
    for path, title in temas:
        if not os.path.exists(path):
            raise FileNotFoundError(f"No se encontró el PDF: {path}")
    if not os.path.exists(portada_path):
        raise FileNotFoundError("No se encontró la portada: portada.pdf")
        
    try:
        from pypdf import PdfReader, PdfWriter
        
        writer = PdfWriter()
        
        # 1. Agregar portada y el índice de temas (normalmente 2 páginas)
        cover_reader = PdfReader(portada_path)
        portada_pages_count = len(cover_reader.pages)
        print(f"   La portada tiene {portada_pages_count} páginas.")
        for page in cover_reader.pages:
            writer.add_page(page)
            
        # Bookmark principal de la portada / índice
        writer.add_outline_item("Índice de Diapositivas", 0)
        
        # 2. Agregar cada tema e ir agregando marcadores
        pagina_actual = portada_pages_count
        
        for path, title in temas:
            reader = PdfReader(path)
            pages_count = len(reader.pages)
            print(f"   Agregando {title} ({pages_count} páginas) en página {pagina_actual + 1}.")
            
            # Agregar páginas
            for page in reader.pages:
                writer.add_page(page)
                
            # Agregar bookmark
            writer.add_outline_item(title, pagina_actual)
            pagina_actual += pages_count
            
        # 3. Guardar el PDF final
        if os.path.exists(final_pdf_path):
            os.remove(final_pdf_path)
            
        with open(final_pdf_path, "wb") as f_out:
            writer.write(f_out)
            
        print(f"   [OK] PDF final de diapositivas creado en: diapositivas/{final_pdf_path}")
        
        # Limpieza
        if os.path.exists(portada_path):
            os.remove(portada_path)
            
        print("   [OK] Archivos temporales eliminados.")
    except Exception as e:
        print(f"   [ERROR] Uniendo PDFs: {e}")
        raise e
    finally:
        os.chdir(dir_original)

def crear_diapositivas_completas():
    print("=== INICIANDO COMPILACIÓN DE DIAPOSITIVAS ===")
    if not check_env():
        return
        
    try:
        crear_portada()
        crear_diapositivas_individuales()
        unir_diapositivas()
        print("\n=== PROCESO DE DIAPOSITIVAS COMPLETADO CON ÉXITO ===")
    except Exception as e:
        print(f"\n[ERROR] Durante el proceso de diapositivas: {e}")

if __name__ == "__main__":
    crear_diapositivas_completas()
