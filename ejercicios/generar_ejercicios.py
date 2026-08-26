import os
import subprocess
import sys
import shutil

def get_conda_env():
    env = os.environ.copy()
    oar_env_dir = r"C:\Users\vacek\anaconda3\envs\oar_env"
    paths_to_add = [
        oar_env_dir,
        os.path.join(oar_env_dir, 'Scripts'),
        os.path.join(oar_env_dir, 'Library', 'bin'),
        os.path.join(oar_env_dir, 'Library', 'usr', 'bin'),
        os.path.join(oar_env_dir, 'Library', 'mingw-w64', 'bin')
    ]
    for p in reversed(paths_to_add):
        if os.path.exists(p):
            env['PATH'] = p + os.pathsep + env['PATH']
    return env

def check_env():
    print("=== VERIFICACIÓN DEL ENTORNO DE EJERCICIOS ===")
    if not os.path.exists("_quarto.yml"):
        print("[ERROR] Este script debe ejecutarse desde la raíz del proyecto.")
        return False
        
    archivos = [
        "ejercicios/portada.qmd",
        "ejercicios/portada.html",
        "ejercicios/_quarto.yml",
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
    print("1. Generando portada con WeasyPrint...")
    dir_original = os.getcwd()
    os.chdir("ejercicios")
    
    try:
        subprocess.run(["quarto", "render", "portada.qmd", "--to", "pdf", "--quiet"], env=get_conda_env(), check=True)
        if not os.path.exists("portada.pdf"):
            raise FileNotFoundError("portada.pdf no fue generado.")
        print("   [OK] Portada creada.")
    except Exception as e:
        print(f"   [ERROR] Creando portada: {e}")
        raise e
    finally:
        os.chdir(dir_original)

def crear_ejercicios():
    print("2. Renderizando libro de ejercicios con Quarto...")
    dir_original = os.getcwd()
    os.chdir("ejercicios")
    
    # Crear configuración temporal sin portada en pdf
    config_temp = """project:
  type: book
  output-dir: ejercicios_pdf

book:
  title: "Ejercicios de Optimización y Análisis de Redes"
  author: 
    - "Víctor Aceña Gil"
    - "Antonio Alonso Ayuso"
  chapters:
    - index.qmd
    - tema1_intro_ejercicios.qmd
    - tema2_opt_no_lineal_ejercicios.qmd
    - tema3_analisis_convexo_ejercicios.qmd
    - tema4_condiciones_optimalidad_ejercicios.qmd
    - tema5_kkt_lp_qp_ejercicios.qmd
    - tema6_grafos_arboles_ejercicios.qmd
    - tema7_caminos_minimos_ejercicios.qmd
    - tema8_flujos_redes_ejercicios.qmd
    - tema9_emparejamiento_redes_ejercicios.qmd
    - tema10_rutas_ejercicios.qmd


format:
  pdf:
    documentclass: scrreprt
    title-block-banner: false 
    toc: true
    toc-title: "Índice de Ejercicios"
    number-sections: false
"""
    
    # Respaldar original
    shutil.copy2("_quarto.yml", "_quarto_original.yml")
    
    # Escribir temporal
    with open("_quarto.yml", "w", encoding="utf-8") as f:
        f.write(config_temp)
        
    try:
        subprocess.run(["quarto", "render"], env=get_conda_env(), check=True)
        print("   [OK] Ejercicios renderizados con éxito.")
    except Exception as e:
        print(f"   [ERROR] Renderizando ejercicios: {e}")
        raise e
    finally:
        # Restaurar original
        shutil.copy2("_quarto_original.yml", "_quarto.yml")
        if os.path.exists("_quarto_original.yml"):
            os.remove("_quarto_original.yml")
        os.chdir(dir_original)

def unir_pdfs(nombre_salida="EjerciciosOptimizacionAnalisisRedes.pdf"):
    print("3. Uniendo PDFs de ejercicios...")
    dir_original = os.getcwd()
    os.chdir("ejercicios")
    
    portada_path = "portada.pdf"
    output_dir = "ejercicios_pdf"
    
    if not os.path.exists(portada_path):
        raise FileNotFoundError("No se encontró ejercicios/portada.pdf")
        
    pdf_files = [f for f in os.listdir(output_dir) if f.endswith(".pdf") and f != nombre_salida]
    if not pdf_files:
        raise FileNotFoundError("No se encontró ningún PDF en ejercicios/ejercicios_pdf/")
        
    book_pdf_name = pdf_files[0]
    book_pdf_path = os.path.join(output_dir, book_pdf_name)
    final_pdf_path = os.path.join(output_dir, nombre_salida)
    
    try:
        from pypdf import PdfReader, PdfWriter
        
        writer = PdfWriter()
        
        # 1. Agregar portada personalizada (1 página)
        cover_reader = PdfReader(portada_path)
        writer.add_page(cover_reader.pages[0])
        
        # 2. Agregar páginas del libro omitiendo la página 1 (portada por defecto de Quarto)
        book_reader = PdfReader(book_pdf_path)
        print(f"   Libro de ejercicios original tiene {len(book_reader.pages)} páginas.")
        
        for page_num in range(1, len(book_reader.pages)):
            writer.add_page(book_reader.pages[page_num])
            
        # 3. Escribir resultado final
        with open(final_pdf_path, "wb") as f_out:
            writer.write(f_out)
            
        print(f"   [OK] PDF final de ejercicios creado en: ejercicios/{final_pdf_path}")
        
        # Limpieza
        if os.path.exists(portada_path):
            os.remove(portada_path)
        if os.path.exists(book_pdf_path):
            os.remove(book_pdf_path)
            
        print("   [OK] Archivos temporales eliminados.")
    except Exception as e:
        print(f"   [ERROR] Uniendo PDFs: {e}")
        raise e
    finally:
        os.chdir(dir_original)

def generar_ejercicios_completos():
    print("=== INICIANDO COMPILACIÓN DE EJERCICIOS ===")
    if not check_env():
        return
        
    try:
        crear_portada()
        crear_ejercicios()
        unir_pdfs()
        print("\n=== PROCESO DE EJERCICIOS COMPLETADO CON ÉXITO ===")
    except Exception as e:
        print(f"\n[ERROR] Durante el proceso de ejercicios: {e}")

if __name__ == "__main__":
    generar_ejercicios_completos()
