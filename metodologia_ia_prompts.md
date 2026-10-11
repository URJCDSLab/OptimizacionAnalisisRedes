# Memoria Metodológica sobre el Uso de Inteligencia Artificial Generativa y Registro de Prompts

**Convocatoria para el Reconocimiento de la Publicación en Acceso Abierto de Materiales Docentes (Curso 2026-2027)**  
*Universidad Rey Juan Carlos*  
*Documento complementario según lo dispuesto en el Anexo III (Apartado 4) y el Anexo VI.*

---

## 1. Identificación de la Obra y del Equipo Docente

* **Título de la obra**: *Optimización y Análisis de Redes: Material Docente en Abierto*
* **Autores**: Víctor Aceña Gil y Antonio Alonso Ayuso
* **Asignatura**: Optimización y Análisis de Redes (Asignatura optativa de 4.º curso, Grado en Matemáticas)
* **Créditos ECTS**: 6.0 ECTS (150 horas de dedicación)
* **Departamento y Centro**: Departamento de Informática y Estadística / Escuela Técnica Superior de Ingeniería Informática (ETSII), Universidad Rey Juan Carlos
* **Grupo de Investigación**: Fundamentos y Aplicaciones de la Ciencia de Datos (DSLAB)
* **Licencia de distribución**: Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)
* **Repositorio institucional**: Archivo Abierto Institucional de la Universidad Rey Juan Carlos (BURJC Digital)
* **Repositorio de código fuente**: <https://github.com/URJCDSLab/OptimizacionAnalisisRedes>

---

## 2. Herramientas de Inteligencia Artificial Generativa Utilizadas

Durante las distintas fases de preparación, maquetación técnica y armonización gráfica del material docente se utilizaron las siguientes herramientas tecnológicas basadas en modelos fundacionales de inteligencia artificial:

1. **Claude 3.5 Sonnet / Claude 3.7 Sonnet (Anthropic)**:
   * Empleado a través del entorno de agente de programación asistida.
   * Utilizado para la estructuración de plantillas en Quarto, depuración de filtros Lua, formateo de tablas y maquetación de llamadas docentes (callouts).
2. **Gemini 2.5 Pro / Advanced (Google DeepMind)**:
   * Empleado en entornos de desarrollo interactivo (Antigravity IDE).
   * Utilizado para la asistencia en la homogeneización tipográfica de expresiones matemáticas LaTeX y generación de código base de scripts de visualización gráfica en Matplotlib.
3. **GitHub Copilot (OpenAI / Microsoft)**:
   * Asistente de autocompletado en el entorno de edición VS Code.
   * Utilizado en la aceleración de sintaxis rutinaria de scripts de automatización en Python (`generar_libro_final.py`, scripts de compilación por lotes).

*Periodo de utilización*: Entre febrero de 2026 y octubre de 2026, correspondiente a la preparación y actualización de los materiales para el curso académico 2026-2027.

---

## 3. Finalidad y Alcance de su Utilización

El uso de sistemas de inteligencia artificial generativa se circunscribió estrictamente a tareas instrumentales de apoyo técnico, soporte informático y asistencia en la maquetación digital:

* **Maquetación y estandarización en Quarto / LaTeX / CSS**: Generación de plantillas CSS (`estilos.css`, `estilos_html.css`) para llamadas visuales (*callouts*) con iconos vectoriales SVG personalizados, adaptación de reglas `@page` para motores de renderizado WeasyPrint y depuración de preámbulos tipográficos en LaTeX.
* **Soporte en código de visualización científica (Matplotlib)**: Generación preliminar de scripts en Python para trazar curvas de nivel discontinuas, proyecciones tridimensionales y flechas vectoriales de gradientes de acuerdo con la paleta cromática corporativa definida en la guía de estilo del proyecto.
* **Estructuración interactiva de animaciones algorítmicas**: Soporte en la codificación de reproductores interactivos en HTML/JavaScript (`images/*_player.html`) para la visualización paso a paso de algoritmos sobre grafos (Ford-Fulkerson, Dijkstra, Árboles Soporte).
* **Revisión ortotipográfica y detección de inconsistencias menores**: Asistencia en la detección de erratas de puntuación, salto de línea en ecuaciones largas y armonización de notación de grafos (diferenciando conjuntos de aristas no dirigidas $\{u, v\}$ de tuplas ordenadas de arcos dirigidos $(u, v)$).

**Lo que NO ha realizado la Inteligencia Artificial**:
* Ningún concepto matemático, definición, teorema, lema o corolario ha sido generado autónomamente por herramientas de inteligencia artificial.
* Toda la secuencia didáctica, el plan de trabajo semanal, los enunciados de los problemas de examen y los casos prácticos de laboratorio han sido concebidos y formulados por los profesores autores.
* La formulación analítica de los modelos y las demostraciones formales provienen íntegramente del conocimiento académico y la experiencia docente de los autores.

---

## 4. Metodología de Trabajo y Supervisión Humana (Human-in-the-Loop)

Para garantizar el máximo rigor científico, pedagógico y ético, se estableció una metodología de supervisión continua estructurada en cuatro niveles:

1. **Diseño directivo y especificación formal previa**:
   * Los profesores autores definieron previamente la guía de estilo docente del libro (`AGENTS.md`), estableciendo restricciones estrictas: prohibición de código de implementación en los capítulos de teoría, prohibición de guiones largos (`—`, `–`), límites en el encadenamiento de cajas de texto, paleta semántica de colores y coherencia estricta de notación.
2. **Validación matemática deductiva paso a paso**:
   * Toda fórmula matemática, sistema de Karush-Kuhn-Tucker, función dual de Lagrange o cálculo de matriz hessiana fue verificado manualmente mediante derivación analítica por los profesores antes de su incorporación al texto definitivo.
3. **Verificación computacional empírica**:
   * Todos los ejemplos numéricos, tablas de iteraciones y algoritmos implementados en Python fueron ejecutados y validados en un entorno virtual aislado reproducible (`oar_env`), comprobando que los resultados arrojados por los solvers (CVXPY, SciPy, NetworkX) coincidían exactamente con los desarrollos expuestos en la teoría.
4. **Inspección tipográfica y control de maquetación**:
   * Cada PDF y documento HTML generado fue inspeccionado visualmente para comprobar la paginación, la correcta resolución de referencias cruzadas (`@fig-*`, `@tbl-*`, `@sec-*`), la ausencia de desbordamientos de ecuaciones y la accesibilidad de los elementos interactivos.

---

## 5. Inventario Representativo de Prompts Utilizados

A continuación se registran ejemplos representativos de los prompts e instrucciones técnicas formuladas a los asistentes de inteligencia artificial generativa durante el desarrollo del proyecto:

### Categoría A: Estandarización de Estilos y Maquetación en Quarto/CSS
```text
"Actúa como asistente de maquetación técnica para Quarto y CSS. 
Necesitamos diseñar una página de créditos institucional formal (A4) que se renderice 
mediante WeasyPrint e incluya los metadatos de la asignatura, el repositorio BURJC Digital, 
la licencia CC BY-SA 4.0 y la declaración obligatoria del Anexo VI de la URJC sobre uso de IA. 
Asegúrate de que la clase CSS tenga márgenes independientes (@page creditos) para que ocupe 
exactamente una página sin desbordar al cuerpo del documento y sin numeración visible."
```

### Categoría B: Scripts de Visualización Geométrica en Matplotlib
```text
"Genera un script en Python con Matplotlib para representar la región factible 
en R^2 definida por tres desigualdades lineales: x1 + 2*x2 <= 8, 2*x1 + x2 <= 8, x1, x2 >= 0. 
El gráfico debe respetar estrictamente nuestra guía de estilo: figsize=(5, 5), set_aspect('equal'), 
curvas de nivel de la función f(x1, x2) = (x1-3)^2 + (x2-3)^2 discontinuas en color '#64748b' con lw=0.5, 
ejes en color '#64748b', espinas superior y derecha ocultas, y el punto óptimo marcado con un círculo negro. 
No utilices guiones largos en los comentarios ni en las etiquetas."
```

### Categoría C: Reproductores Interactivos para Animaciones Algorítmicas
```text
"Diseña una interfaz web minimalista en HTML y JavaScript autónomo para servir como 
reproductor de una animación GIF paso a paso del Algoritmo de Ford-Fulkerson en redes de flujo. 
El reproductor debe contener botones estilizados para: Anterior, Play/Pausa, Siguiente, Reiniciar, 
una barra deslizante de progreso interactiva y un indicador numérico que muestre la fase actual 
y el flujo acumulado en cada paso. La tipografía debe ser Inter o sans-serif nativa de sistema."
```

### Categoría D: Automatización y Comprobación de Paginación en Python
```text
"Escribe una función en Python usando pypdf que combine seis documentos PDF independientes 
(portada, índice, guía de estudio, apuntes, diapositivas y problemas resueltos) en un único 
volumen maestro. La función debe calcular iterativamente los números de página de inicio de cada 
sección para inyectarlos en la plantilla del índice general hasta que los números de página 
converjan, y construir el árbol jerárquico de marcadores (outlines) de navegación PDF."
```

---

## 6. Declaración de Responsabilidad Ética e Intelectual

Los autores, **Víctor Aceña Gil** y **Antonio Alonso Ayuso**, declaran bajo su exclusiva y personal responsabilidad que:

1. El uso de las herramientas de inteligencia artificial generativa se ha limitado a tareas de apoyo auxiliar, técnico y de maquetación, sin delegar en ningún caso la autoría intelectual, el rigor deductivo ni la responsabilidad docente del contenido.
2. Todo el material ha sido exhaustivamente revisado, comprobado y validado en sus dimensiones científica, didáctica y normativa.
3. El contenido respeta plenamente los derechos de propiedad intelectual de terceros y se distribuye íntegramente bajo la licencia abierta Creative Commons Reconocimiento-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).
