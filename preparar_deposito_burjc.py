import os
import shutil
import zipfile

def preparar_deposito():
    out_dir = os.path.abspath('deposito_burjc')
    os.makedirs(out_dir, exist_ok=True)
    print(f"Directorio de depósito: {out_dir}")

    # 1. Copiar PDF Maestro del libro
    src_book = os.path.abspath(r'libro\Optimizacion_y_Analisis_de_Redes.pdf')
    dst_book = os.path.join(out_dir, 'Optimizacion_y_Analisis_de_Redes.pdf')
    if os.path.exists(src_book):
        shutil.copy2(src_book, dst_book)
        sz = os.path.getsize(dst_book) / (1024 * 1024)
        print(f"[OK] 1. Fichero Principal: Optimizacion_y_Analisis_de_Redes.pdf ({sz:.2f} MB)")
    else:
        print(f"[ERROR] No se encuentra {src_book}")

    # 2. Generar software_laboratorios.zip
    dst_soft_zip = os.path.join(out_dir, 'software_laboratorios.zip')
    soft_src = os.path.abspath(r'..\OptimizacionAnalisisRedes_software')
    if os.path.exists(soft_src):
        with zipfile.ZipFile(dst_soft_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(soft_src):
                if '.git' in root:
                    continue
                for f in files:
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, soft_src)
                    zf.write(full, rel)
        sz = os.path.getsize(dst_soft_zip) / (1024 * 1024)
        print(f"[OK] 2. Fichero Complementario 1: software_laboratorios.zip ({sz:.2f} MB)")
    else:
        print(f"[ERROR] No se encuentra {soft_src}")

    # 3. Generar materiales_editables.zip
    dst_mat_zip = os.path.join(out_dir, 'materiales_editables.zip')
    include_dirs = ['guia_estudio', 'apuntes', 'diapositivas', 'ejercicios', 'ejercicios_resueltos', 'laboratorios', 'images', 'libro']
    include_files = ['_quarto.yml', 'References.bib', 'estilos.css', 'estilos_html.css', 'diapo_theme.scss', 'metodologia_ia_prompts.md', 'README.md']
    
    with zipfile.ZipFile(dst_mat_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in include_files:
            if os.path.exists(f):
                zf.write(f, f)
        for d in include_dirs:
            if not os.path.exists(d):
                continue
            for root, dirs, files in os.walk(d):
                if any(x in root for x in ['.git', '.quarto', '__pycache__']):
                    continue
                for f in files:
                    ext = os.path.splitext(f)[1].lower()
                    if ext in ['.pdf', '.html', '.aux', '.log', '.tex', '.synctex.gz', '.nav', '.snm', '.toc', '.out']:
                        continue
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, '.')
                    zf.write(full, rel)
    sz = os.path.getsize(dst_mat_zip) / (1024 * 1024)
    print(f"[OK] 3. Fichero Complementario 2: materiales_editables.zip ({sz:.2f} MB)")



    # 5. Escribir archivo de instrucciones y metadatos para copiar y pegar
    meta_txt = os.path.join(out_dir, 'METADATOS_Y_SOLICITUD_BURJC.txt')
    contenido_meta = """================================================================================
METADATOS Y TEXTOS PARA EL DEPÓSITO EN BURJC DIGITAL Y SEDE ELECTRÓNICA URJC
Convocatoria Publicación Acceso Abierto Materiales Docentes 2026-2027
================================================================================

1. ARCHIVOS A SUBIR A BURJC DIGITAL
------------------------------------
Fichero Principal:
  - Optimizacion_y_Analisis_de_Redes.pdf (1.365 páginas, volumen unificado maestro con todo el contenido: Guía, Apuntes, Diapositivas, Ejercicios, Soluciones y Software)

Ficheros Complementarios:
  - materiales_editables.zip (Fuentes editables .qmd, .bib, imágenes y memoria de IA)
  - software_laboratorios.zip (Cuadernos y código de los 10 laboratorios en Python)


2. METADATOS PARA EL FORMULARIO DE BURJC DIGITAL
-------------------------------------------------
TÍTULO:
Optimización y Análisis de Redes: Material docente en abierto para el Grado en Matemáticas (4.º curso)

AUTORES:
Aceña Gil, Víctor; Alonso Ayuso, Antonio; Martínez Moguerza, Javier; López Cano, Emilio

ASIGNATURA:
Optimización y Análisis de Redes (Asignatura optativa de 4.º curso, 6.0 ECTS)

TITULACIÓN Y CENTRO:
Grado en Matemáticas. Escuela Técnica Superior de Ingeniería Informática (ETSII). Universidad Rey Juan Carlos.

FECHA:
2026-10 (o Curso 2026-2027)

LICENCIA:
Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)

MATERIAS / PALABRAS CLAVE:
Optimización matemática; Análisis de redes; Teoría de grafos; Programación no lineal; Condiciones KKT; Dualidad lagrangiana; Programación convexa disciplinada; Algoritmos de caminos mínimos; Flujos en redes; Problema del viajante de comercio; Python; CVXPY; NetworkX

RESUMEN / ABSTRACT:
Material docente en acceso abierto correspondiente a la asignatura optativa de 4.º curso "Optimización y Análisis de Redes" del Grado en Matemáticas de la Universidad Rey Juan Carlos (6.0 ECTS). La obra integra de forma exhaustiva los fundamentos de la optimización matemática continua y el modelado discreto mediante teoría de redes, articulando el rigor deductivo formal con la computación científica aplicada en Python.

La publicación comprende cinco componentes interconectados organizados en seis partes con portadillas editoriales de sección: (1) Guía de estudio detallada para las 15 semanas lectivas (25 páginas) con planificación sesión a sesión (teoría y laboratorio), objetivos según la taxonomía de Bloom, contenidos, materiales específicos con referencia a secciones temáticas y recomendación de trabajo autónomo personal; (2) Manual teórico de apuntes (432 páginas) con 10 temas exhaustivos, demostraciones formales, más de 80 figuras geométricas vectoriales y animaciones algorítmicas interactivas; (3) Conjunto de presentaciones docentes en diapositivas dinámicas (709 transparencias) con diseño paralelo en columnas y resolución analítica detallada; (4) Colección de ejercicios prácticos clasificados por temas (43 páginas); (5) Cuaderno exhaustivo de problemas resueltos paso a paso (146 páginas) con tablas pivotadas y comprobaciones analíticas; y (6) Software docente y entorno computacional en Python estructurado en cuadernos Jupyter con soporte para CVXPY, SciPy y NetworkX, tests unitarios automatizados y preservación en Software Heritage.

Todo el material se distribuye bajo la licencia abierta Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).


3. DECLARACIÓN DEL SOFTWARE (CATEGORÍA 6)
------------------------------------------
En el campo de Descripción / Notas de BURJC Digital:
"Archivo con código fuente (software_laboratorios.zip), depositado en Software Heritage con el SWHID:
swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504
Enlace permanente en Software Heritage:
https://archive.softwareheritage.org/swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504;origin=https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software;visit=swh:1:snp:ebc85597ce189b4bf17381fae325419b947cdb24;anchor=swh:1:rev:a16debd4c8b8c2d4c16f297bfd3d401fbee0f2af
Repositorio público en GitHub:
https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software"


4. ENLACES PARA LA SOLICITUD EN LA SEDE ELECTRÓNICA URJC (ANEXO II)
--------------------------------------------------------------------
- Depósito institucional (BURJC Digital): [Pegar la URL generada tras depositar]
- Repositorio principal de materiales (GitHub): https://github.com/URJCDSLab/OptimizacionAnalisisRedes
- Repositorio de software docente (GitHub): https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software
- Identificador persistente Software Heritage (SWHID): swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504
- Enlace permanente Software Heritage: https://archive.softwareheritage.org/swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504;origin=https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software;visit=swh:1:snp:ebc85597ce189b4bf17381fae325419b947cdb24;anchor=swh:1:rev:a16debd4c8b8c2d4c16f297bfd3d401fbee0f2af


5. ANEXO V: CONSENTIMIENTO DE DOCENTES (DOCUMENTO OBLIGATORIO A FIRMAR)
-----------------------------------------------------------------------
Este texto debe plasmarse en documento para ser firmado electrónicamente por los 3 profesores que imparten la asignatura en el curso 2026-2027:

----------------------------- INICIO PLANTILLA ANEXO V -----------------------------
ANEXO V: Consentimiento de docentes

Esta es la plantilla que se utilizará como documento para atestiguar el consentimiento de las personas que son docentes de las asignaturas que se mencionan en la convocatoria. En el caso de asignaturas extraordinarias, no se incluirá la primera parte, correspondiente a las asignaturas en que se imparten, pero sí la segunda, correspondiente a la autoría.

Este documento corresponde con una solicitud presentada a la Convocatoria de la Universidad Rey Juan Carlos para el reconocimiento de la publicación de materiales docentes en acceso abierto. Los materiales presentados en esa solicitud se imparten en las siguientes asignaturas:
GRADO EN MATEMÁTICAS (MÓSTOLES) - OPTIMIZACIÓN Y ANÁLISIS DE REDES - 2Q

Los siguientes profesores y profesoras, con docencia en las mencionadas asignaturas, están debidamente informados de esta solicitud, y de los términos y condiciones de la mencionada Convocatoria:
Víctor Aceña Gil, victor.acena@urjc.es
Javier Martínez Moguerza, javier.moguerza@urjc.es
Emilio López Cano, emilio.lopez@urjc.es

Así mismo, entre ellos, los siguientes son autores de los materiales presentados a la Convocatoria, en los porcentajes aproximados que se indica:
Víctor Aceña Gil, victor.acena@urjc.es, 90%
Javier Martínez Moguerza, javier.moguerza@urjc.es, 5%
Emilio López Cano, emilio.lopez@urjc.es, 5%

Y para que así conste, firman, a fecha de la firma electrónica.
------------------------------ FIN PLANTILLA ANEXO V ------------------------------


6. NOTA ACLARATORIA DE AUTORÍA (PARA LA SEDE ELECTRÓNICA / ANEXO II)
--------------------------------------------------------------------
En el formulario web de solicitud (Anexo II), en el campo de "Observaciones" o "Justificación de autoría":

"Nota sobre autoría y procedencia de los materiales:
La obra publicada en BURJC Digital y preservada en Software Heritage reconoce en su portada la coautoría intelectual del Prof. Antonio Alonso Ayuso por ser el autor de los materiales base originales desarrollados en cursos precedentes. La presente edición unificada para el curso 2026-2027 ha sido coordinada y desarrollada por el profesor Víctor Aceña Gil (90% de autoría docente), contando con la colaboración y revisión del equipo docente que imparte la asignatura en el curso actual, Javier Martínez Moguerza (5%) y Emilio López Cano (5%), conforme a las Bases 5.3 y 7.b de la convocatoria y según consta en el documento de consentimiento y autoría (Anexo V)."
================================================================================

"""
    with open(meta_txt, 'w', encoding='utf-8') as f:
        f.write(contenido_meta)
    print(f"[OK] 5. Instrucciones y metadatos: METADATOS_Y_SOLICITUD_BURJC.txt")
    print("\n¡Todo el paquete de depósito está listo en la carpeta 'deposito_burjc'!")

if __name__ == '__main__':
    preparar_deposito()
