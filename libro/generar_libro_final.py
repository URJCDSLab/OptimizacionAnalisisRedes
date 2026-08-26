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
        "ejercicios_resueltos/generar_soluciones.py",
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
    try:
        python_oar = r"C:\Users\vacek\anaconda3\envs\oar_env\python.exe"
        subprocess.run([python_oar, path], env=get_conda_env(), check=True)
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
    ejecutar_script("ejercicios_resueltos/generar_soluciones.py")
    ejecutar_script("laboratorios/generar_software.py")


def compilar_libro_completo(nombre_salida="LibroCompletoOptimizacionAnalisisRedes.pdf"):
    print("2. Calculando páginas de inicio y compilando Libro Completo...")
    
    from pypdf import PdfReader, PdfWriter
    
    guia_path = "guia_estudio/GuiaEstudioOptimizacionAnalisisRedes.pdf"
    apuntes_path = "apuntes/apuntes_pdf/ApuntesOptimizacionAnalisisRedes.pdf"
    diapositivas_path = "diapositivas/diapositivas_pdf/DiapositivasOptimizacionAnalisisRedes.pdf"
    ejercicios_path = "ejercicios/ejercicios_pdf/EjerciciosOptimizacionAnalisisRedes.pdf"
    soluciones_path = "ejercicios_resueltos/soluciones_pdf/SolucionesOptimizacionAnalisisRedes.pdf"
    software_path = "laboratorios/SoftwareUtilizadoOptimizacionAnalisisRedes.pdf"
    
    # Verificar que existen todos los PDFs
    paths = [guia_path, apuntes_path, diapositivas_path, ejercicios_path, soluciones_path, software_path]
    for p in paths:
        if not os.path.exists(p):
            raise FileNotFoundError(f"Falta el PDF de componente: {p}")
            
    # Leer número de páginas de cada PDF
    len_guia = len(PdfReader(guia_path).pages)
    len_apuntes = len(PdfReader(apuntes_path).pages)
    len_diapositivas = len(PdfReader(diapositivas_path).pages)
    len_ejercicios = len(PdfReader(ejercicios_path).pages)
    len_soluciones = len(PdfReader(soluciones_path).pages)
    len_software = len(PdfReader(software_path).pages)
    
    print(f"   Páginas de componentes: Guía={len_guia}, Apuntes={len_apuntes}, Diapositivas={len_diapositivas}, Ejercicios={len_ejercicios}, Soluciones={len_soluciones}, Software={len_software}")
    
    len_portada = 1
    len_indice = 2 # Suposición inicial

    # Bucle iterativo para calcular páginas de inicio estables
    for i in range(4):
        guia_page = len_portada + len_indice + 1
        apuntes_page = guia_page + len_guia
        diapositivas_page = apuntes_page + len_apuntes
        ejercicios_page = diapositivas_page + len_diapositivas
        soluciones_page = ejercicios_page + len_ejercicios
        software_page = soluciones_page + len_soluciones

        # Generar indice.qmd temporal
        with open("libro/indice.qmd", "r", encoding="utf-8") as f:
            template = f.read()

        # Reemplazos de secciones principales
        indice_content = template.replace("{{GUIA_PAGE}}", str(guia_page))
        indice_content = indice_content.replace("{{APUNTES_PAGE}}", str(apuntes_page))
        indice_content = indice_content.replace("{{DIAPOSITIVAS_PAGE}}", str(diapositivas_page))
        indice_content = indice_content.replace("{{EJERCICIOS_PAGE}}", str(ejercicios_page))
        indice_content = indice_content.replace("{{SOLUCIONES_PAGE}}", str(soluciones_page))
        indice_content = indice_content.replace("{{SOFTWARE_PAGE}}", str(software_page))

        # Guía de Estudio
        indice_content = indice_content.replace("{{GUIA_P1}}", str(guia_page))
        indice_content = indice_content.replace("{{GUIA_P2}}", str(guia_page + 2))
        indice_content = indice_content.replace("{{GUIA_P3}}", str(guia_page + 13))

        # Apuntes Teóricos (offsets internos exactos)
        indice_content = indice_content.replace("{{APUNTES_T1}}", str(apuntes_page - 1 + 6))
        indice_content = indice_content.replace("{{APUNTES_T2}}", str(apuntes_page - 1 + 18))
        indice_content = indice_content.replace("{{APUNTES_T3}}", str(apuntes_page - 1 + 49))
        indice_content = indice_content.replace("{{APUNTES_T4}}", str(apuntes_page - 1 + 93))
        indice_content = indice_content.replace("{{APUNTES_T5}}", str(apuntes_page - 1 + 159))
        indice_content = indice_content.replace("{{APUNTES_T6}}", str(apuntes_page - 1 + 199))
        indice_content = indice_content.replace("{{APUNTES_T7}}", str(apuntes_page - 1 + 258))
        indice_content = indice_content.replace("{{APUNTES_T8}}", str(apuntes_page - 1 + 294))
        indice_content = indice_content.replace("{{APUNTES_T9}}", str(apuntes_page - 1 + 352))
        indice_content = indice_content.replace("{{APUNTES_T10}}", str(apuntes_page - 1 + 383))
        indice_content = indice_content.replace("{{APUNTES_CONCL}}", str(apuntes_page - 1 + 421))
        indice_content = indice_content.replace("{{APUNTES_REF}}", str(apuntes_page - 1 + 424))

        # Diapositivas de Clase
        indice_content = indice_content.replace("{{DIAPO_T1}}", str(diapositivas_page - 1 + 3))
        indice_content = indice_content.replace("{{DIAPO_T2}}", str(diapositivas_page - 1 + 18))
        indice_content = indice_content.replace("{{DIAPO_T3}}", str(diapositivas_page - 1 + 92))
        indice_content = indice_content.replace("{{DIAPO_T4}}", str(diapositivas_page - 1 + 162))
        indice_content = indice_content.replace("{{DIAPO_T5}}", str(diapositivas_page - 1 + 268))
        indice_content = indice_content.replace("{{DIAPO_T6}}", str(diapositivas_page - 1 + 350))
        indice_content = indice_content.replace("{{DIAPO_T7}}", str(diapositivas_page - 1 + 460))
        indice_content = indice_content.replace("{{DIAPO_T8}}", str(diapositivas_page - 1 + 537))
        indice_content = indice_content.replace("{{DIAPO_T9}}", str(diapositivas_page - 1 + 537))
        indice_content = indice_content.replace("{{DIAPO_T10}}", str(diapositivas_page - 1 + 626))

        # Ejercicios Prácticos
        indice_content = indice_content.replace("{{EJ_T1}}", str(ejercicios_page - 1 + 6))
        indice_content = indice_content.replace("{{EJ_T2}}", str(ejercicios_page - 1 + 8))
        indice_content = indice_content.replace("{{EJ_T3}}", str(ejercicios_page - 1 + 12))
        indice_content = indice_content.replace("{{EJ_T4}}", str(ejercicios_page - 1 + 16))
        indice_content = indice_content.replace("{{EJ_T5}}", str(ejercicios_page - 1 + 21))
        indice_content = indice_content.replace("{{EJ_T6}}", str(ejercicios_page - 1 + 24))
        indice_content = indice_content.replace("{{EJ_T7}}", str(ejercicios_page - 1 + 29))
        indice_content = indice_content.replace("{{EJ_T8}}", str(ejercicios_page - 1 + 32))
        indice_content = indice_content.replace("{{EJ_T9}}", str(ejercicios_page - 1 + 35))
        indice_content = indice_content.replace("{{EJ_T10}}", str(ejercicios_page - 1 + 39))

        # Problemas Resueltos
        indice_content = indice_content.replace("{{SOL_T1}}", str(soluciones_page - 1 + 6))
        indice_content = indice_content.replace("{{SOL_T2}}", str(soluciones_page - 1 + 11))
        indice_content = indice_content.replace("{{SOL_T3}}", str(soluciones_page - 1 + 27))
        indice_content = indice_content.replace("{{SOL_T4}}", str(soluciones_page - 1 + 43))
        indice_content = indice_content.replace("{{SOL_T5}}", str(soluciones_page - 1 + 68))
        indice_content = indice_content.replace("{{SOL_T6}}", str(soluciones_page - 1 + 80))
        indice_content = indice_content.replace("{{SOL_T7}}", str(soluciones_page - 1 + 97))
        indice_content = indice_content.replace("{{SOL_T8}}", str(soluciones_page - 1 + 106))
        indice_content = indice_content.replace("{{SOL_T9}}", str(soluciones_page - 1 + 117))
        indice_content = indice_content.replace("{{SOL_T10}}", str(soluciones_page - 1 + 132))

        # Software y Laboratorios
        indice_content = indice_content.replace("{{LAB_1}}", str(software_page - 1 + 2))
        indice_content = indice_content.replace("{{LAB_2}}", str(software_page - 1 + 2))
        indice_content = indice_content.replace("{{LAB_3}}", str(software_page - 1 + 2))
        indice_content = indice_content.replace("{{LAB_4}}", str(software_page - 1 + 3))
        indice_content = indice_content.replace("{{LAB_5}}", str(software_page - 1 + 3))
        indice_content = indice_content.replace("{{LAB_6}}", str(software_page - 1 + 3))
        indice_content = indice_content.replace("{{LAB_7}}", str(software_page - 1 + 4))
        indice_content = indice_content.replace("{{LAB_8}}", str(software_page - 1 + 4))
        indice_content = indice_content.replace("{{LAB_9}}", str(software_page - 1 + 4))
        indice_content = indice_content.replace("{{LAB_10}}", str(software_page - 1 + 4))

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

    print(f"   Páginas de inicio estables calculadas: Índice={len_portada+1}, Guía={guia_page}, Apuntes={apuntes_page}, Diapositivas={diapositivas_page}, Ejercicios={ejercicios_page}, Soluciones={soluciones_page}, Software={software_page}")

    # 3. Combinar todo
    print("3. Combinando todos los PDFs en el documento final...")
    writer = PdfWriter()

    pdfs_a_unir = [
        ("libro/portada.pdf", "Portada", []),
        ("libro/indice_temp.pdf", "Índice General", []),
        (guia_path, "Guía de Estudio", [
            ("Presentación, competencias y metodología", guia_page - 1),
            ("Cronograma semanal (Bloques I y II)", guia_page + 2 - 1),
            ("Sistema de evaluación y bibliografía", guia_page + 13 - 1)
        ]),
        (apuntes_path, "Apuntes Teóricos", [
            ("Tema 1: Introducción a la investigación operativa", apuntes_page - 1 + 6 - 1),
            ("Tema 2: Optimización no lineal", apuntes_page - 1 + 18 - 1),
            ("Tema 3: Análisis convexo", apuntes_page - 1 + 49 - 1),
            ("Tema 4: Condiciones de optimalidad y KKT", apuntes_page - 1 + 93 - 1),
            ("Tema 5: Programación lineal y cuadrática", apuntes_page - 1 + 159 - 1),
            ("Tema 6: Grafos y árboles soporte", apuntes_page - 1 + 199 - 1),
            ("Tema 7: Problema del camino mínimo", apuntes_page - 1 + 258 - 1),
            ("Tema 8: Flujos en redes", apuntes_page - 1 + 294 - 1),
            ("Tema 9: Emparejamientos en redes", apuntes_page - 1 + 352 - 1),
            ("Tema 10: Rutas eulerianas, hamiltonianas, TSP y VRP", apuntes_page - 1 + 383 - 1),
            ("Conclusiones", apuntes_page - 1 + 421 - 1),
            ("Bibliografía", apuntes_page - 1 + 424 - 1)
        ]),
        (diapositivas_path, "Diapositivas de Clase", [
            ("Tema 1: Introducción a la investigación operativa", diapositivas_page - 1 + 3 - 1),
            ("Tema 2: Optimización no lineal", diapositivas_page - 1 + 18 - 1),
            ("Tema 3: Análisis convexo", diapositivas_page - 1 + 92 - 1),
            ("Tema 4: Condiciones de optimalidad y KKT", diapositivas_page - 1 + 162 - 1),
            ("Tema 5: Programación lineal y cuadrática", diapositivas_page - 1 + 268 - 1),
            ("Tema 6: Grafos y árboles soporte", diapositivas_page - 1 + 350 - 1),
            ("Tema 7: Problema del camino mínimo", diapositivas_page - 1 + 460 - 1),
            ("Tema 9: Emparejamientos en redes", diapositivas_page - 1 + 537 - 1),
            ("Tema 10: Rutas eulerianas, hamiltonianas, TSP y VRP", diapositivas_page - 1 + 626 - 1)
        ]),
        (ejercicios_path, "Ejercicios Prácticos", [
            ("Tema 1: Introducción a la investigación operativa", ejercicios_page - 1 + 6 - 1),
            ("Tema 2: Optimización no lineal", ejercicios_page - 1 + 8 - 1),
            ("Tema 3: Análisis convexo", ejercicios_page - 1 + 12 - 1),
            ("Tema 4: Condiciones de optimalidad y KKT", ejercicios_page - 1 + 16 - 1),
            ("Tema 5: Dualidad KKT en LP y QP", ejercicios_page - 1 + 21 - 1),
            ("Tema 6: Grafos y árboles soporte", ejercicios_page - 1 + 24 - 1),
            ("Tema 7: Problema del camino mínimo", ejercicios_page - 1 + 29 - 1),
            ("Tema 8: Flujos en redes", ejercicios_page - 1 + 32 - 1),
            ("Tema 9: Emparejamientos en redes", ejercicios_page - 1 + 35 - 1),
            ("Tema 10: Rutas eulerianas, hamiltonianas, TSP y VRP", ejercicios_page - 1 + 39 - 1)
        ]),
        (soluciones_path, "Problemas Resueltos", [
            ("Soluciones Tema 1: Introducción", soluciones_page - 1 + 6 - 1),
            ("Soluciones Tema 2: Optimización no lineal", soluciones_page - 1 + 11 - 1),
            ("Soluciones Tema 3: Análisis convexo", soluciones_page - 1 + 27 - 1),
            ("Soluciones Tema 4: Condiciones KKT", soluciones_page - 1 + 43 - 1),
            ("Soluciones Tema 5: Dualidad LP y QP", soluciones_page - 1 + 68 - 1),
            ("Soluciones Tema 6: Grafos y árboles soporte", soluciones_page - 1 + 80 - 1),
            ("Soluciones Tema 7: Problema del camino mínimo", soluciones_page - 1 + 97 - 1),
            ("Soluciones Tema 8: Flujos en redes", soluciones_page - 1 + 106 - 1),
            ("Soluciones Tema 9: Emparejamientos en redes", soluciones_page - 1 + 117 - 1),
            ("Soluciones Tema 10: Rutas eulerianas, hamiltonianas, TSP y VRP", soluciones_page - 1 + 132 - 1)
        ]),
        (software_path, "Software y Laboratorios", [
            ("Laboratorio 1: Cálculo simbólico con SymPy", software_page - 1 + 2 - 1),
            ("Laboratorio 2: Optimización no lineal con Python", software_page - 1 + 2 - 1),
            ("Laboratorio 3: Análisis de convexidad y CVXPY", software_page - 1 + 2 - 1),
            ("Laboratorio 4: Condiciones KKT en Python", software_page - 1 + 3 - 1),
            ("Laboratorio 5: Dualidad KKT y QP en Python", software_page - 1 + 3 - 1),
            ("Laboratorio 6: Grafos y MST en Python", software_page - 1 + 3 - 1),
            ("Laboratorio 7: Camino mínimo en Python", software_page - 1 + 4 - 1),
            ("Laboratorio 8: Flujos en redes en Python", software_page - 1 + 4 - 1),
            ("Laboratorio 9: Emparejamientos en redes en Python", software_page - 1 + 4 - 1),
            ("Laboratorio 10: Rutas eulerianas, TSP y VRP en Python", software_page - 1 + 4 - 1)
        ])
    ]

    pagina_acumulada = 0
    secciones_bookmarks = []

    # 1. Agregar todas las páginas
    for path, title, subitems in pdfs_a_unir:
        reader = PdfReader(path)
        pages_count = len(reader.pages)
        secciones_bookmarks.append((title, pagina_acumulada, subitems))

        for page in reader.pages:
            writer.add_page(page)

        pagina_acumulada += pages_count

    # 2. Agregar todos los marcadores jerárquicos
    for title, sec_page_idx, subitems in secciones_bookmarks:
        sec_bookmark = writer.add_outline_item(title, sec_page_idx)
        for sub_title, sub_page_idx in subitems:
            writer.add_outline_item(sub_title, sub_page_idx, parent=sec_bookmark)

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
