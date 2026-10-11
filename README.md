# Optimización y Análisis de Redes: Material Docente y Libro de Referencia

**Material docente en abierto de la Universidad Rey Juan Carlos**

* **Título de la obra:** Optimización y Análisis de Redes (Libro de Texto y Material Docente Completo)
* **Autores:** Víctor Aceña Gil y Antonio Alonso Ayuso
* **Asignatura:** Optimización y Análisis de Redes (Asignatura optativa de 4.º curso)
* **Titulación:** Grado en Matemáticas (Escuela Técnica Superior de Ingeniería Informática, Universidad Rey Juan Carlos)
* **Créditos ECTS:** 6.0 ECTS (150 horas de dedicación total)
* **Fecha de edición:** Curso académico 2026-2027 (Junio 2026)
* **Lugar de depósito:** Archivo Abierto Institucional de la URJC (**BURJC Digital**) - <https://burjcdigital.urjc.es/>
* **Identificador / Handle institucional:** `PENDIENTE_DE_REGISTRO_BURJC`
* **Preservación de software docente (Software Heritage):**
  * Repositorio de software (Categoría 6): <https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software>
  * Identificador persistente (SWHID): [`swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504`](https://archive.softwareheritage.org/swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504;origin=https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software;visit=swh:1:snp:ebc85597ce189b4bf17381fae325419b947cdb24;anchor=swh:1:rev:a16debd4c8b8c2d4c16f297bfd3d401fbee0f2af)
  * [![Archived on Software Heritage](https://archive.softwareheritage.org/badge/swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504/)](https://archive.softwareheritage.org/swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504;origin=https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software;visit=swh:1:snp:ebc85597ce189b4bf17381fae325419b947cdb24;anchor=swh:1:rev:a16debd4c8b8c2d4c16f297bfd3d401fbee0f2af)
* **Grupo de investigación:** Fundamentos y Aplicaciones de la Ciencia de Datos (DSLAB, URJC)

---

## 1. Descripción General del Repositorio

Este repositorio reúne la colección completa, integrada y autosuficiente de materiales docentes para la asignatura **Optimización y Análisis de Redes**, impartida como optativa de cuarto curso en el Grado en Matemáticas de la Universidad Rey Juan Carlos (URJC).

La obra cubre tanto los fundamentos teóricos, geométricos y analíticos de la optimización matemática continua y discreta como su vertiente computacional aplicada mediante Python (`NumPy`, `SciPy`, `CVXPY`, `NetworkX`, `SymPy`, `PuLP`).

El contenido se distribuye de forma accesible en dos formatos complementarios:

1. **Sitio web interactivo**: Publicado en el directorio `docs/`, permitiendo la consulta abierta en línea con reproductores interactivos para la ejecución paso a paso de animaciones y algoritmos.
2. **Libro maestro unificado en PDF**: Obra editorial completa de 1.363 páginas que agrupa en un único volumen encuadernado digitalmente la guía de estudio, los apuntes teóricos, las diapositivas de clase, los enunciados de ejercicios, las soluciones analíticas desarrolladas y los cuadernos de laboratorio, disponible directamente en [`libro/Optimizacion_y_Analisis_de_Redes.pdf`](libro/Optimizacion_y_Analisis_de_Redes.pdf).

---

## 2. Estructura Temática de la Asignatura

El plan docente se estructura en dos bloques temáticos secuenciales que comprenden diez capítulos:

### Bloque I: Optimización no lineal
* **Tema 1: Introducción a la Programación No Lineal**: Fundamentos, modelos clásicos de decisión (Cournot, Markowitz, transporte) y tipología de problemas no lineales.
* **Tema 2: Optimización no lineal y métodos numéricos**: Análisis diferencial local, métodos de búsqueda lineal unidimensional (Dicotómica, Sección Áurea, Fibonacci) y algoritmos multivariantes sin restricciones (Coordenadas Cíclicas, Máximo Descenso, Newton y BFGS).
* **Tema 3: Análisis convexo y geometría de la optimización**: Conjuntos convexos, funciones convexas, conos (cono normal, cono tangente) y teoremas de separación e hiperplanos de soporte.
* **Tema 4: Condiciones de optimalidad (KKT)**: Cualificación de restricciones (LICQ), condiciones necesarias y suficientes de primer y segundo orden de Karush-Kuhn-Tucker.
* **Tema 5: Dualidad y programación cuadrática**: Dualidad lagrangiana en Programación Lineal y Cuadrática, condiciones de punto de silla y el método del Símplex de Wolfe.

### Bloque II: Optimización en redes
* **Tema 6: Introducción a la teoría de grafos y árboles**: Matrices de incidencia y adyacencia, propiedad de Total Unimodularidad (TUM), árboles soporte de mínimo peso (Kruskal, Prim) y agrupamiento (*clustering*) basado en MST.
* **Tema 7: Caminos mínimos**: Formulación primal-dual, potenciales nodales, algoritmos de Dijkstra, Bellman-Ford (detección de ciclos negativos) y Floyd-Warshall.
* **Tema 8: Flujos en redes**: Teorema Max-Flow Min-Cut, algoritmos de Ford-Fulkerson y Edmonds-Karp, y problemas de flujo de coste mínimo (algoritmo del ciclo negativo y Simplex de redes).
* **Tema 9: Emparejamientos y asignación óptima**: Emparejamientos en grafos bipartitos y generales, algoritmo Húngaro para asignación y algoritmo de Blossom de Edmonds.
* **Tema 10: Rutas eulerianas, hamiltonianas y enrutamiento (TSP y VRP)**: Circuitos eulerianos (algoritmo de Fleury y Hierholzer), problema del cartero chino, formulaciones enteras del TSP (DFJ y MTZ), heurísticas (2-Opt), aproximación de Christofides y taxonomía del problema de rutas de vehículos con capacidad (CVRP).

---

## 3. Componentes del Repositorio (Estructura en 6 Partes)

El repositorio se organiza de forma modular a través de [Quarto](https://quarto.org/), correspondiéndose con las seis partes del libro unificado:

* **Parte I: Guía de Estudio (`guia_estudio/`)**:
  * Cronograma detallado semana a semana (Semanas 1 a 15) formulado con verbos de la taxonomía de Bloom.
  * Desglose por sesiones de los materiales específicos de estudio (apuntes, diapositivas, ejercicios y laboratorios).
  * Recomendación sistemática de trabajo autónomo del estudiante (3 horas por sesión, 6 horas semanales, 150 horas totales equivalentes a 6.0 ECTS).
  * Documento en PDF: [`guia_estudio/GuiaEstudioOptimizacionAnalisisRedes.pdf`](guia_estudio/GuiaEstudioOptimizacionAnalisisRedes.pdf).

* **Parte II: Apuntes Teóricos (`apuntes/` y `tema1.qmd` a `tema10.qmd`)**:
  * Tratado teórico formal y riguroso con demostraciones matemáticas completas, intuición geométrica y ejemplos paso a paso.
  * Ilustraciones vectoriales de alta resolución generadas con Matplotlib bajo una guía de estilo cromática homogénea.
  * Documento en PDF: [`apuntes/apuntes_pdf/ApuntesOptimizacionAnalisisRedes.pdf`](apuntes/apuntes_pdf/ApuntesOptimizacionAnalisisRedes.pdf).

* **Parte III: Diapositivas de Clase (`diapositivas/`)**:
  * *Formato HTML (RevealJS)*: Presentaciones dinámicas para el aula con trazas algorítmicas paso a paso y reproductores interactivos.
  * *Formato PDF (Beamer)*: Presentaciones sintéticas optimizadas para estudio fuera de línea e impresión ([`diapositivas/diapositivas_pdf/DiapositivasOptimizacionAnalisisRedes.pdf`](diapositivas/diapositivas_pdf/DiapositivasOptimizacionAnalisisRedes.pdf)).

* **Parte IV: Ejercicios Prácticos - Enunciados (`ejercicios/`)**:
  * Colección completa de problemas teóricos y numéricos propuestos por tema, ordenados por dificultad pedagógica.
  * Documento en PDF: [`ejercicios/ejercicios_pdf/EjerciciosOptimizacionAnalisisRedes.pdf`](ejercicios/ejercicios_pdf/EjerciciosOptimizacionAnalisisRedes.pdf).

* **Parte V: Soluciones de Ejercicios (`ejercicios_resueltos/`)**:
  * Resoluciones analíticas paso a paso, justificaciones algebraicas y comprobaciones numéricas completas de los problemas propuestos.
  * Documento en PDF: [`ejercicios_resueltos/soluciones_pdf/SolucionesOptimizacionAnalisisRedes.pdf`](ejercicios_resueltos/soluciones_pdf/SolucionesOptimizacionAnalisisRedes.pdf).

* **Parte VI: Software y Laboratorios (`laboratorios/`)**:
  * 10 cuadernos computacionales interactivos en Python diseñados para implementar algoritmos y resolver modelos con bibliotecas científicas de referencia.
  * Código fuente preservado en Software Heritage con SWHID: [`swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504`](https://archive.softwareheritage.org/swh:1:dir:85b3015deeb96b2949cfbeea61e1558c1c8b9504;origin=https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software;visit=swh:1:snp:ebc85597ce189b4bf17381fae325419b947cdb24;anchor=swh:1:rev:a16debd4c8b8c2d4c16f297bfd3d401fbee0f2af).
  * Documento en PDF: [`laboratorios/SoftwareUtilizadoOptimizacionAnalisisRedes.pdf`](laboratorios/SoftwareUtilizadoOptimizacionAnalisisRedes.pdf).
  * Repositorio específico de programas: <https://github.com/URJCDSLab/OptimizacionAnalisisRedes_software>.

* **Volumen Maestro Unificado (`libro/`)**:
  * Fusión editorial de las seis partes precedentes con portadillas de sección independientes, cálculo iterativo de páginas estables y marcadores PDF (*bookmarks*) jerárquicos.
  * Documento en PDF: [`libro/Optimizacion_y_Analisis_de_Redes.pdf`](libro/Optimizacion_y_Analisis_de_Redes.pdf) (1.363 páginas).

---

## 4. Requisitos de Software y Compilación

Para reproducir los cuadernos, previsualizar los materiales web o recompilar el libro completo, se recomienda utilizar un entorno aislado de Python gestionado mediante Conda.

### 4.1. Creación del entorno

```bash
conda create -n oar_env python=3.11 -y
conda activate oar_env
```

### 4.2. Instalación de dependencias científicas

```bash
pip install numpy scipy matplotlib networkx cvxpy sympy autograd pulp pypdf jupyter
```

### 4.3. Visualización con Quarto CLI

Teniendo instalado [Quarto CLI](https://quarto.org/docs/get-started/) (v1.4 o superior):

```bash
# Previsualizar el sitio web en tiempo real
quarto preview

# Renderizar el sitio web completo en la carpeta docs/
quarto render
```

### 4.4. Compilación del Libro Maestro Unificado

Para recompilar todo el libro y mantener sincronizados los apuntes, diapositivas Beamer, presentaciones RevealJS HTML, ejercicios y el PDF unificado final:

```bash
conda activate oar_env
python libro/generar_libro_final.py
```

---

## 5. Declaración sobre Uso de Herramientas de Inteligencia Artificial Generativa

En cumplimiento de lo dispuesto en el Anexo III.4 y el Anexo VI de la *Convocatoria para el reconocimiento de la publicación en acceso abierto de materiales docentes del curso 2026-2027* de la Universidad Rey Juan Carlos, se formula la siguiente declaración sobre el uso de herramientas de inteligencia artificial generativa:

1. **Tipo de herramientas utilizadas:** Modelos de lenguaje de gran tamaño (LLM) y asistentes de codificación (Claude 3.5 Sonnet, Gemini 2.5 Pro y GitHub Copilot).
2. **Forma y alcance del uso:** Las herramientas se emplearon exclusivamente como asistencia auxiliar para la estandarización de plantillas en Quarto, el soporte en la sintaxis de scripts de visualización con Matplotlib, la revisión ortotipográfica y la comprobación de coherencia en la notación matemática LaTeX.
3. **Grado de uso:** Carácter instrumental y de apoyo técnico y de formato. La totalidad de los contenidos matemáticos, definiciones, teoremas, demostraciones analíticas, diseño curricular, ejercicios y guías docentes han sido concebidos y desarrollados íntegramente por los autores.

Para un desglose exhaustivo de los prompts representativos, el registro de interacción y la metodología de supervisión humana (*Human-in-the-Loop*), consúltese la memoria complementaria: [`metodologia_ia_prompts.md`](metodologia_ia_prompts.md).

**Manifiesto de autoría:** Todo el material ha sido verificado, validado y aprobado por los profesores autores, quienes asumen la total responsabilidad científica y académica sobre la obra.

---

## 6. Derechos de Autor y Licencia

**Copyright © 2026 Víctor Aceña Gil y Antonio Alonso Ayuso.**

<a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es"><img src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" alt="Licencia de Creative Commons" style="border-width:0"/></a>

**Esta obra se distribuye bajo una licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)**.  
El texto legal completo de la licencia se encuentra disponible en: <https://creativecommons.org/licenses/by-sa/4.0/deed.es>.
