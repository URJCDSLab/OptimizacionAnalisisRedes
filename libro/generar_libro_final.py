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
    print("=== VERIFICACIÓN DEL ENTORNO GENERAL ===")
    if not os.path.exists("_quarto.yml"):
        print("[ERROR] Este script debe ejecutarse desde la raíz del proyecto.")
        return False
        
    archivos = [
        "libro/portada.html",
        "libro/portada.qmd",
        "libro/indice.qmd",
        "guia_estudio/generar_guia.py",
        "apuntes/generar_apuntes.py",
        "diapositivas/crear_diapositivas_completas.py",
        "ejercicios/generar_ejercicios.py",
        "laboratorios/generar_software.py",
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

def ejecutar_script(path):
    print(f"Ejecutando script de subcomponente: {path}...")
    dir_original = os.getcwd()
    # Cambiar al directorio correspondiente si es necesario
    # Pero los scripts esperan ser ejecutados desde la raiz del proyecto
    try:
        subprocess.run([sys.executable, path], env=get_conda_env(), check=True)
        print(f"   [OK] {path} completado con éxito.")
    except Exception as e:
        print(f"   [ERROR] Ejecutando {path}: {e}")
        raise e

def generar_subcomponentes():
    print("1. Ejecutando la generación de todos los subcomponentes...")
    ejecutar_script("guia_estudio/generar_guia.py")
    ejecutar_script("apuntes/generar_apuntes.py")
    ejecutar_script("diapositivas/crear_diapositivas_completas.py")
    ejecutar_script("ejercicios/generar_ejercicios.py")
    ejecutar_script("laboratorios/generar_software.py")

def compilar_libro_completo(nombre_salida="LibroCompletoOptimizacionAnalisisRedes.pdf"):
    print("2. Calculando páginas de inicio y compilando Libro Completo...")
    
    from pypdf import PdfReader, PdfWriter
    
    guia_path = "guia_estudio/GuiaEstudioOptimizacionAnalisisRedes.pdf"
    apuntes_path = "apuntes/apuntes_pdf/ApuntesOptimizacionAnalisisRedes.pdf"
    diapositivas_path = "diapositivas/diapositivas_pdf/DiapositivasOptimizacionAnalisisRedes.pdf"
    ejercicios_path = "ejercicios/ejercicios_pdf/EjerciciosOptimizacionAnalisisRedes.pdf"
    software_path = "laboratorios/SoftwareUtilizadoOptimizacionAnalisisRedes.pdf"
    
    # Verificar que existen todos los PDFs
    paths = [guia_path, apuntes_path, diapositivas_path, ejercicios_path, software_path]
    for p in paths:
        if not os.path.exists(p):
            raise FileNotFoundError(f"Falta el PDF de componente: {p}")
            
    # Leer número de páginas de cada PDF
    len_guia = len(PdfReader(guia_path).pages)
    len_apuntes = len(PdfReader(apuntes_path).pages)
    len_diapositivas = len(PdfReader(diapositivas_path).pages)
    len_ejercicios = len(PdfReader(ejercicios_path).pages)
    len_software = len(PdfReader(software_path).pages)
    
    print(f"   Páginas de componentes: Guía={len_guia}, Apuntes={len_apuntes}, Diapositivas={len_diapositivas}, Ejercicios={len_ejercicios}, Software={len_software}")
    
    len_portada = 1
    len_indice = 1 # Suposición inicial
    
    # Bucle iterativo para calcular páginas de inicio estables
    for i in range(3):
        guia_page = len_portada + len_indice + 1
        apuntes_page = guia_page + len_guia
        diapositivas_page = apuntes_page + len_apuntes
        ejercicios_page = diapositivas_page + len_diapositivas
        software_page = ejercicios_page + len_ejercicios
        
        # Generar indice.qmd temporal
        with open("libro/indice.qmd", "r", encoding="utf-8") as f:
            template = f.read()
            
        indice_content = template.replace("{{GUIA_PAGE}}", str(guia_page))
        indice_content = indice_content.replace("{{APUNTES_PAGE}}", str(apuntes_page))
        indice_content = indice_content.replace("{{DIAPOSITIVAS_PAGE}}", str(diapositivas_page))
        indice_content = indice_content.replace("{{EJERCICIOS_PAGE}}", str(ejercicios_page))
        indice_content = indice_content.replace("{{SOFTWARE_PAGE}}", str(software_page))
        
        with open("libro/indice_temp.qmd", "w", encoding="utf-8") as f:
            f.write(indice_content)
            
        # Renderizar portada e indice temporales en libro/
        dir_original = os.getcwd()
        os.chdir("libro")
        try:
            # Portada
            subprocess.run(["quarto", "render", "portada.qmd", "--to", "pdf", "--quiet"], env=get_conda_env(), check=True)
            # Índice
            subprocess.run(["quarto", "render", "indice_temp.qmd", "--to", "pdf", "--quiet"], env=get_conda_env(), check=True)
        finally:
            os.chdir(dir_original)
            
        # Medir tamaño real del índice compilado
        real_len_indice = len(PdfReader("libro/indice_temp.pdf").pages)
        if real_len_indice == len_indice:
            break
        else:
            len_indice = real_len_indice
            
    print(f"   Páginas de inicio estables calculadas: Índice={len_portada+1}, Guía={guia_page}, Apuntes={apuntes_page}, Diapositivas={diapositivas_page}, Ejercicios={ejercicios_page}, Software={software_page}")
    
    # 3. Combinar todo
    print("3. Combinando todos los PDFs en el documento final...")
    writer = PdfWriter()
    
    pdfs_a_unir = [
        ("libro/portada.pdf", "Portada"),
        ("libro/indice_temp.pdf", "Índice General"),
        (guia_path, "Guía de Estudio"),
        (apuntes_path, "Apuntes Teóricos"),
        (diapositivas_path, "Diapositivas de Clase"),
        (ejercicios_path, "Ejercicios Prácticos"),
        (software_path, "Software Utilizado")
    ]
    
    bookmarks_info = []
    pagina_acumulada = 0
    
    for path, title in pdfs_a_unir:
        reader = PdfReader(path)
        pages_count = len(reader.pages)
        # Registrar info de marcadores
        bookmarks_info.append((title, pagina_acumulada))
        
        for page in reader.pages:
            writer.add_page(page)
            
        pagina_acumulada += pages_count
        
    # Añadir marcadores
    for title, page_idx in bookmarks_info:
        writer.add_outline_item(title, page_idx)
        
    final_output_path = os.path.join("libro", nombre_salida)
    if os.path.exists(final_output_path):
        os.remove(final_output_path)
        
    with open(final_output_path, "wb") as f_out:
        writer.write(f_out)
        
    print(f"   [OK] Libro completo guardado en: {final_output_path}")
    
    # 4. Limpieza
    print("4. Limpiando archivos temporales...")
    temporales = [
        "libro/portada.pdf",
        "libro/indice_temp.qmd",
        "libro/indice_temp.pdf"
    ]
    for temp in temporales:
        if os.path.exists(temp):
            os.remove(temp)
            
    print("   [OK] Archivos temporales eliminados con éxito.")
    
    # Resumen
    info_size = os.path.getsize(final_output_path) / 1024 / 1024
    print(f"\n==============================================")
    print(f"       LIBRO COMPLETO GENERADO CON ÉXITO")
    print(f"==============================================")
    print(f"Archivo: {final_output_path}")
    print(f"Páginas totales: {pagina_acumulada}")
    print(f"Tamaño: {round(info_size, 2)} MB")
    print(f"==============================================")

def generar_todo():
    print("=== INICIANDO PROCESO GLOBAL DE COMPILACIÓN ===")
    if not check_env():
        return
        
    try:
        generar_subcomponentes()
        compilar_libro_completo()
        print("\n=== PROCESO COMPLETO FINALIZADO CON ÉXITO ===")
    except Exception as e:
        print(f"\n[ERROR] Durante el proceso global: {e}")

if __name__ == "__main__":
    generar_todo()
