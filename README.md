# Optimización y Análisis de Redes

**Material docente oficial y libro de referencia**  
*Grado en Matemáticas (Universidad Rey Juan Carlos)*  

**Autores:** Víctor Aceña Gil y Antonio Alonso Ayuso  
*Departamento de Informática y Estadística / Grupo de Investigación DSLAB (URJC)*

---

## Descripción del Repositorio

Este repositorio contiene la colección completa de materiales docentes para la asignatura de **Optimización y Análisis de Redes** impartida en el Grado en Matemáticas de la Universidad Rey Juan Carlos (URJC).

La obra cubre tanto los fundamentos teóricos, geométricos y analíticos de la optimización matemática continua y discreta como su vertiente computacional aplicada mediante Python (`SciPy`, `CVXPY`, `NetworkX`, `SymPy`).

El contenido está disponible en dos formatos principales:

1. **Sitio web interactivo**: Publicado a partir del directorio `docs/`, permitiendo la lectura en línea con reproductores interactivos para las animaciones y algoritmos.
2. **Libro completo en PDF**: Documento unificado y encuadernado digitalmente de más de 1.300 páginas que agrupa la guía de estudio, apuntes, diapositivas, ejercicios y laboratorios, accesible directamente en [`libro/LibroCompletoOptimizacionAnalisisRedes.pdf`](libro/LibroCompletoOptimizacionAnalisisRedes.pdf).

---

## Estructura de la Asignatura

El temario se organiza en dos bloques temáticos secuenciales a lo largo de diez capítulos:

### Bloque I: Optimización no lineal
* **Tema 1: Introducción a la Programación No Lineal**: Fundamentos, modelos clásicos de decisión (Cournot, Markowitz, transporte) y tipología de problemas no lineales.
* **Tema 2: Optimización no lineal y métodos numéricos**: Análisis diferencial local, métodos de búsqueda lineal unidimensional (Dicotómica, Sección Áurea, Fibonacci) y algoritmos multivariantes sin restricciones (Coordenadas Cíclicas, Máximo Descenso, Newton y BFGS).
* **Tema 3: Análisis convexo y geometría de la optimización**: Conjuntos convexos, funciones convexas, conos (cono normal, cono tangente) y teoremas de separación.
* **Tema 4: Condiciones de optimalidad (KKT)**: Cualificación de restricciones (LICQ), condiciones necesarias y suficientes de primer y segundo orden de Karush-Kuhn-Tucker.
* **Tema 5: Dualidad y programación cuadrática**: Dualidad lagrangiana en Programación Lineal y Cuadrática, condiciones de punto de silla y el método del Símplex de Wolfe.

### Bloque II: Optimización en redes
* **Tema 6: Introducción a la teoría de grafos y árboles**: Matrices de incidencia y adyacencia, propiedad de Total Unimodularidad (TUM), árboles soporte de mínimo peso (Kruskal, Prim) y clustering basado en MST.
* **Tema 7: Caminos mínimos**: Formulación primal-dual, potenciales nodales, algoritmos de Dijkstra, Bellman-Ford (detección de ciclos negativos) y Floyd-Warshall.
* **Tema 8: Flujos en redes**: Teorema Max-Flow Min-Cut, algoritmos de Ford-Fulkerson y Edmonds-Karp, y problemas de flujo de coste mínimo (algoritmo del ciclo negativo y Simplex de redes).
* **Tema 9: Emparejamientos y asignación óptima**: Emparejamientos en grafos bipartitos y generales, algoritmo Húngaro para asignación y algoritmo de Blossom de Edmonds.
* **Tema 10: Rutas eulerianas, hamiltonianas y enrutamiento (TSP y VRP)**: Circuitos eulerianos (algoritmo de Fleury y Hierholzer), problema del cartero chino, formulaciones del TSP (DFJ y MTZ), heurísticas (2-Opt), aproximación de Christofides y taxonomía del problema de rutas de vehículos (VRP).

---

## Componentes del Repositorio

El repositorio se divide en módulos independientes desarrollados en [Quarto](https://quarto.org/):

* **Apuntes Teóricos (`tema1.qmd` a `tema10.qmd`)**: Texto riguroso con demostraciones detalladas, ejemplos numéricos resueltos e ilustraciones geométricas.
* **Diapositivas (`diapositivas/`)**:
  * *HTML (RevealJS)*: Presentaciones interactivas para el aula con trazas algorítmicas paso a paso y reproductores dinámicos.
  * *PDF (Beamer)*: Presentaciones compactas y estáticas listas para descarga e impresión (`diapositivas/diapositivas_pdf/DiapositivasOptimizacionAnalisisRedes.pdf`).
* **Ejercicios Prácticos (`ejercicios/`)**: Colección completa de enunciados de problemas analíticos propuestos por tema (`ejercicios/ejercicios_pdf/EjerciciosOptimizacionAnalisisRedes.pdf`).
* **Laboratorios Computacionales (`laboratorios/`)**: 10 cuadernos interactivos en Python diseñados para que el estudiante aprenda a implementar y resolver modelos con bibliotecas científicas (`laboratorios/SoftwareUtilizadoOptimizacionAnalisisRedes.pdf`).
* **Guía de Estudio (`guia_estudio/`)**: Cronograma docente, distribución de sesiones, metodología pedagógica y sistema de evaluación (`guia_estudio/GuiaEstudioOptimizacionAnalisisRedes.pdf`).
* **Libro Unificado (`libro/`)**: Script maestro y PDF unificado final que integra secuencialmente todos los componentes del curso.

---

## Requisitos y Entorno de Software

Para trabajar con los cuadernos interactivos y reproducir los laboratorios, se recomienda utilizar un entorno de Python 3.11 o superior gestionado mediante Conda.

### Creación del entorno

```bash
conda create -n oar_env python=3.11 -y
conda activate oar_env
```

### Instalación de dependencias científicas

```bash
pip install numpy scipy matplotlib networkx cvxpy sympy autograd
```

### Visualización y renderizado con Quarto

Para previsualizar o compilar la versión web localmente, se requiere tener instalado [Quarto CLI](https://quarto.org/docs/get-started/) (v1.4 o superior):

```bash
# Previsualizar el sitio web en tiempo real
quarto preview

# Renderizar el sitio web completo en la carpeta docs/
quarto render
```

---

## Licencia y Créditos

Este material ha sido desarrollado por **Víctor Aceña Gil** y **Antonio Alonso Ayuso** dentro del grupo de investigación de alto rendimiento en Fundamentos y Aplicaciones de la Ciencia de Datos ([DSLAB](https://dslab.urjc.es/)) de la Universidad Rey Juan Carlos.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" alt="Licencia de Creative Commons" style="border-width:0"/></a><br />
Esta obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">licencia de Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)</a>.
