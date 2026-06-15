import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx
from scipy.optimize import minimize

# Ensure output directory exists
output_dir = r"C:\Users\vacek\Proyectos\OptimizacionAnalisisRedes\images"
os.makedirs(output_dir, exist_ok=True)

# Styling configuration
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# Colors
C_PRIMARY = '#0284c7'     # Cerulean
C_BG = '#f0f9ff'          # Light sky blue
C_BORDER = '#0284c7'
C_TEXT = '#0f172a'        # Slate 900
C_TEXT_MUTED = '#64748b'  # Slate 500
C_ALERT = '#ef4444'       # Red/Orange Coral
C_SUCCESS = '#10b981'     # Emerald Green
C_ACCENT = '#f59e0b'      # Amber

def save_fig(name):
    plt.tight_layout()
    path = os.path.join(output_dir, name)
    plt.savefig(path, bbox_inches='tight', dpi=300, transparent=True)
    plt.close()
    print(f"Generated: {name}")

# ==========================================
# 1. TEMA 2: Búsqueda Unidimensional (Bisección)
# ==========================================
def gen_opt_1d_biseccion():
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(0.2, 3.8, 200)
    f = lambda x: (x - 2.2)**2 + 1.2
    
    ax.plot(x, f(x), color=C_PRIMARY, lw=2.5, label=r'$f(x)$')
    
    # Points
    a, b = 0.5, 3.5
    x1, x2 = 1.5, 2.7
    
    points = {'a': a, 'x_1': x1, 'x_2': x2, 'b': b}
    
    for label, px in points.items():
        py = f(px)
        ax.plot(px, py, 'o', color=C_PRIMARY, markersize=8, zorder=5)
        ax.vlines(px, 0, py, colors=C_TEXT_MUTED, linestyles='dashed', alpha=0.6)
        ax.text(px, -0.15, f'${label}$', ha='center', va='top', fontsize=12, color=C_TEXT, fontweight='bold')
    
    # Highlight interval reduction
    # New interval is [a, x2] since f(x1) < f(x2)
    ax.axvspan(a, x2, color=C_BG, alpha=0.5, label='Nuevo intervalo $[a, x_2]$')
    ax.axvspan(x2, b, color='#fee2e2', alpha=0.4, label='Intervalo descartado $[x_2, b]$')
    
    ax.set_ylim(0, 5)
    ax.set_xlim(0, 4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    ax.set_xticks([])
    ax.set_ylabel(r'$f(x)$', fontsize=12, color=C_TEXT)
    ax.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none')
    
    save_fig('opt_1d_biseccion.png')

# ==========================================
# 2. TEMA 3: Conjuntos Convexos
# ==========================================
def gen_conjuntos_convexos():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    # Convex Set (Ellipse)
    t = np.linspace(0, 2*np.pi, 100)
    x_conv = 3 * np.cos(t) + 4
    y_conv = 2 * np.sin(t) + 4
    ax1.fill(x_conv, y_conv, color=C_BG, edgecolor=C_PRIMARY, lw=2)
    
    # Segment in Convex
    p1, p2 = np.array([2.5, 3.5]), np.array([5.5, 4.5])
    ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], color=C_ALERT, lw=2.5, marker='o', markersize=8, zorder=5)
    ax1.text(p1[0]-0.3, p1[1], '$x$', ha='right', va='center', fontsize=12, fontweight='bold')
    ax1.text(p2[0]+0.3, p2[1], '$y$', ha='left', va='center', fontsize=12, fontweight='bold')
    ax1.text(4.0, 4.3, r'$[x,y] \subset S$', color=C_ALERT, fontsize=12, ha='center', va='bottom')
    ax1.set_title('Conjunto Convexo', fontsize=14, color=C_TEXT, pad=15)
    ax1.axis('off')
    ax1.set_xlim(0, 8)
    ax1.set_ylim(0, 8)
    
    # Non-Convex Set (L-Shape)
    x_nc = [1, 5, 5, 2, 2, 1, 1]
    y_nc = [1, 1, 3, 3, 6, 6, 1]
    ax2.fill(x_nc, y_nc, color=C_BG, edgecolor=C_PRIMARY, lw=2)
    
    # Segment in Non-Convex
    q1, q2 = np.array([1.5, 5.0]), np.array([4.0, 1.5])
    ax2.plot([q1[0], q2[0]], [q1[1], q2[1]], color=C_ALERT, lw=2.5, marker='o', markersize=8, zorder=5)
    ax2.text(q1[0]-0.2, q1[1], '$x$', ha='right', va='center', fontsize=12, fontweight='bold')
    ax2.text(q2[0]+0.2, q2[1], '$y$', ha='left', va='center', fontsize=12, fontweight='bold')
    ax2.text(3.1, 3.5, r'$[x,y] \not\subset S$', color=C_ALERT, fontsize=12, ha='center', va='bottom')
    ax2.set_title('Conjunto NO Convexo', fontsize=14, color=C_TEXT, pad=15)
    ax2.axis('off')
    ax2.set_xlim(0, 8)
    ax2.set_ylim(0, 8)
    
    save_fig('conjuntos_convexos.png')

# ==========================================
# 3. TEMA 3: Epígrafe
# ==========================================
def gen_epigrafo():
    fig, ax = plt.subplots(figsize=(7, 5))
    x = np.linspace(-2, 2, 200)
    f = lambda x: 0.5 * x**2 + 1
    
    # Plot function
    ax.plot(x, f(x), color=C_PRIMARY, lw=3, label=r'$f(x)$')
    
    # Shade Epigraph
    ax.fill_between(x, f(x), 4.5, color=C_BG, alpha=0.7, label=r'$\mathrm{epi}(f) = \{(x, y) \mid y \geq f(x)\}$')
    
    # Secant line
    x1, x2 = -1.2, 1.5
    y1, y2 = f(x1), f(x2)
    ax.plot([x1, x2], [y1, y2], color=C_ALERT, lw=2, marker='o', markersize=6, zorder=5)
    
    # Point on secant
    t = 0.4
    xt = (1-t)*x1 + t*x2
    yt_sec = (1-t)*y1 + t*y2
    yt_fun = f(xt)
    
    ax.plot([xt, xt], [yt_fun, yt_sec], color=C_TEXT_MUTED, linestyle='dotted')
    ax.plot(xt, yt_sec, 'o', color=C_ALERT, markersize=6)
    ax.plot(xt, yt_fun, 'o', color=C_PRIMARY, markersize=6)
    
    # Text labels
    ax.text(xt+0.1, yt_sec+0.1, r'$(1-\lambda)f(x) + \lambda f(y)$', color=C_ALERT, fontsize=10)
    ax.text(xt+0.1, yt_fun-0.2, r'$f((1-\lambda)x + \lambda y)$', color=C_PRIMARY, fontsize=10)
    ax.text(x1-0.1, y1, r'$x$', ha='right', fontsize=12, color=C_TEXT)
    ax.text(x2+0.1, y2, r'$y$', ha='left', fontsize=12, color=C_TEXT)
    
    ax.set_ylim(0, 5)
    ax.set_xlim(-2.5, 2.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(loc='upper center', frameon=True, facecolor='white', edgecolor='none')
    
    save_fig('epigrafo.png')

# ==========================================
# 4. TEMA 4: Cono de Direcciones
# ==========================================
def gen_cono_direcciones():
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Circular sector / wedge
    theta = np.linspace(0, np.pi/2, 100)
    r = 4.0
    x_feas = r * np.cos(theta)
    y_feas = r * np.sin(theta)
    x_poly = [0] + list(x_feas) + [0]
    y_poly = [0] + list(y_feas) + [0]
    ax.fill(x_poly, y_poly, color=C_BG, edgecolor=C_PRIMARY, lw=2, label=r'Región Factible $\Omega$')
    
    # Boundary point x*
    x_star = np.array([4.0 * np.cos(np.pi/4), 4.0 * np.sin(np.pi/4)])
    ax.plot(x_star[0], x_star[1], 'o', color=C_ALERT, markersize=8, zorder=10)
    ax.text(x_star[0]+0.15, x_star[1]+0.15, '$x^*$', fontsize=12, color=C_TEXT, fontweight='bold')
    
    # Draw tangent line at x*
    tx = np.linspace(1, 5, 100)
    ty = 4 * np.sqrt(2) - tx
    ax.plot(tx, ty, color=C_TEXT_MUTED, linestyle='dashed')
    
    n = x_star / np.linalg.norm(x_star)
    ax.quiver(x_star[0], x_star[1], n[0], n[1], scale=5, color=C_ALERT, zorder=5, label='Normal exterior $\\nabla g(x^*)$')
    
    # Draw some feasible directions
    d1 = np.array([-1.5, -0.5])
    d2 = np.array([-0.5, -1.5])
    ax.quiver(x_star[0], x_star[1], d1[0], d1[1], scale=4, scale_units='xy', color=C_SUCCESS, zorder=5, width=0.007)
    ax.quiver(x_star[0], x_star[1], d2[0], d2[1], scale=4, scale_units='xy', color=C_SUCCESS, zorder=5, width=0.007)
    ax.text(x_star[0] + d1[0]/1.5, x_star[1] + d1[1]/1.5 - 0.2, r'$d \in F(x^*)$', color=C_SUCCESS, fontsize=10, ha='right')
    
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(loc='upper right')
    
    save_fig('cono_direcciones.png')

# ==========================================
# 5. TEMA 4: Condiciones KKT
# ==========================================
def gen_condiciones_kkt():
    fig, ax = plt.subplots(figsize=(6, 6))
    
    theta = np.linspace(0, 2*np.pi, 200)
    ax.fill(3*np.cos(theta), 3*np.sin(theta), color=C_BG, edgecolor=C_PRIMARY, lw=2, label=r'$g(x) \leq 0$')
    
    ang = np.pi / 4
    x_star = np.array([3*np.cos(ang), 3*np.sin(ang)])
    ax.plot(x_star[0], x_star[1], 'o', color=C_ALERT, markersize=8, zorder=10)
    ax.text(x_star[0]+0.15, x_star[1]+0.15, '$x^*$', fontsize=12, fontweight='bold', color=C_TEXT)
    
    grad_g = x_star / np.linalg.norm(x_star)
    grad_f = -grad_g
    
    ax.quiver(x_star[0], x_star[1], grad_g[0], grad_g[1], scale=4, color=C_ALERT, zorder=5, label='$\\nabla g(x^*)$ (Activa)')
    ax.quiver(x_star[0], x_star[1], grad_f[0], grad_f[1], scale=4, color=C_PRIMARY, zorder=5, label='$-\\nabla f(x^*)$')
    
    ax.text(x_star[0] + grad_g[0]*0.5, x_star[1] + grad_g[1]*0.5 + 0.1, '$\\nabla g(x^*)$', color=C_ALERT, fontsize=11)
    ax.text(x_star[0] + grad_f[0]*0.5, x_star[1] + grad_f[0]*0.5 - 0.2, '$-\\nabla f(x^*)$', color=C_PRIMARY, fontsize=11)
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(loc='lower left')
    
    save_fig('condiciones_kkt.png')

# ==========================================
# 6. TEMA 5: Región Factible LP
# ==========================================
def gen_region_factible_lp():
    fig, ax = plt.subplots(figsize=(7, 6))
    
    x1 = np.linspace(0, 5, 200)
    y1 = (8 - x1) / 2.0
    y2 = (12 - 3*x1) / 2.0
    
    ax.plot(x1, y1, color=C_PRIMARY, lw=2, label=r'$x_1 + 2x_2 = 8$')
    ax.plot(x1, y2, color=C_ACCENT, lw=2, label=r'$3x_1 + 2x_2 = 12$')
    
    y_feas = np.minimum(y1, y2)
    ax.fill_between(x1, 0, np.maximum(0, y_feas), where=(x1 <= 4), color=C_BG, alpha=0.7)
    
    opt_x, opt_y = 2, 3
    ax.plot(opt_x, opt_y, 'o', color=C_ALERT, markersize=8, zorder=5)
    ax.text(opt_x+0.1, opt_y+0.1, r'Óptimo $(2,3)$', color=C_ALERT, fontweight='bold', fontsize=11)
    
    cx = np.linspace(0, 5, 100)
    for z in [2, 3.5, 5]:
        ax.plot(cx, z - cx, color=C_TEXT_MUTED, linestyle='dotted', alpha=0.7)
    ax.quiver(1, 1, 0.7, 0.7, scale=8, color=C_TEXT_MUTED, width=0.005)
    ax.text(1.5, 1.6, r'Dirección de $\max c^T x$', color=C_TEXT_MUTED, fontsize=9, rotation=45)
    
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 5.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    ax.set_xlabel(r'$x_1$', fontsize=12, color=C_TEXT)
    ax.set_ylabel(r'$x_2$', fontsize=12, color=C_TEXT)
    ax.legend(loc='upper right')
    
    save_fig('region_factible_lp.png')

# ==========================================
# 7. TEMA 6: Regresión Robusta (L1 vs L2)
# ==========================================
def gen_regresion_robusta():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    np.random.seed(42)
    X = np.linspace(1, 10, 15)
    y = 1.2 * X + 2 + np.random.normal(0, 0.4, 15)
    
    y[2] += 6.5
    y[11] += 5.0
    
    w_l2 = np.polyfit(X, y, 1)
    line_l2 = w_l2[0] * X + w_l2[1]
    
    def l1_loss(w):
        return np.sum(np.abs(y - (w[0] * X + w[1])))
    
    res = minimize(l1_loss, [1.0, 1.0])
    w_l1 = res.x
    line_l1 = w_l1[0] * X + w_l1[1]
    
    outliers = [2, 11]
    inliers = [i for i in range(len(X)) if i not in outliers]
    
    ax.scatter(X[inliers], y[inliers], color=C_PRIMARY, s=50, label='Datos estándar', zorder=5)
    ax.scatter(X[outliers], y[outliers], color=C_ACCENT, s=80, marker='X', label='Outliers (Ruido)', zorder=5)
    
    ax.plot(X, line_l2, color=C_ALERT, lw=2, linestyle='dashed', label=r'Ajuste $L_2$ (Mínimos Cuadrados)')
    ax.plot(X, line_l1, color=C_SUCCESS, lw=2.5, label=r'Ajuste $L_1$ (Robusto)')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    ax.set_xlabel('Variable Predictora ($x$)', fontsize=11, color=C_TEXT)
    ax.set_ylabel('Variable Respuesta ($y$)', fontsize=11, color=C_TEXT)
    ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='none')
    
    save_fig('regresion_robusta.png')

# ==========================================
# 8. TEMA 7: Puentes de Königsberg
# ==========================================
def gen_puentes_konigsberg():
    fig, ax = plt.subplots(figsize=(6, 5))
    
    nodes = {
        'A': (0, 1.5),
        'D': (-1.5, 0),
        'C': (1.5, 0),
        'B': (0, -1.5)
    }
    
    for name, pos in nodes.items():
        rect = patches.Circle(pos, 0.25, facecolor=C_BG, edgecolor=C_PRIMARY, lw=2, zorder=5)
        ax.add_patch(rect)
        ax.text(pos[0], pos[1], name, color=C_TEXT, ha='center', va='center', fontweight='bold', fontsize=12, zorder=6)
        
    def draw_edge_curve(p1, p2, rad, color=C_TEXT_MUTED, lw=1.5):
        style = f"Arc3,rad={rad}"
        ax.annotate(
            '', xy=p2, xytext=p1,
            arrowprops=dict(
                arrowstyle="-",
                connectionstyle=style,
                color=color,
                lw=lw,
                shrinkA=8,
                shrinkB=8
            ),
            zorder=2
        )
        
    draw_edge_curve(nodes['A'], nodes['D'], -0.2)
    draw_edge_curve(nodes['A'], nodes['D'], 0.2)
    draw_edge_curve(nodes['B'], nodes['D'], -0.2)
    draw_edge_curve(nodes['B'], nodes['D'], 0.2)
    draw_edge_curve(nodes['A'], nodes['C'], -0.1)
    draw_edge_curve(nodes['B'], nodes['C'], 0.1)
    draw_edge_curve(nodes['C'], nodes['D'], 0.0)
    
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    save_fig('puentes_konigsberg.png')

# ==========================================
# 9. TEMA 7: MST (Kruskal/Prim)
# ==========================================
def gen_kruskal_prim_mst():
    fig, ax = plt.subplots(figsize=(7, 5))
    
    G = nx.Graph()
    edges = [
        ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 5),
        ('C', 'D', 8), ('C', 'E', 10), ('D', 'E', 2), ('D', 'F', 6),
        ('E', 'F', 3)
    ]
    G.add_weighted_edges_from(edges)
    
    pos = {
        'A': (0, 1),
        'B': (1, 2),
        'C': (1, 0),
        'D': (3, 2),
        'E': (3, 0),
        'F': (4.2, 1)
    }
    
    mst = nx.minimum_spanning_tree(G)
    mst_edges = set(mst.edges())
    
    mst_list = []
    other_list = []
    for u, v in G.edges():
        if (u, v) in mst_edges or (v, u) in mst_edges:
            mst_list.append((u, v))
        else:
            other_list.append((u, v))
            
    nx.draw_networkx_nodes(G, pos, node_color=C_BG, edgecolors=C_PRIMARY, node_size=600, linewidths=2, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=11, font_color=C_TEXT, font_weight='bold', ax=ax)
    
    nx.draw_networkx_edges(G, pos, edgelist=other_list, width=1.5, edge_color='#cbd5e1', style='dashed', ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=mst_list, width=3.5, edge_color=C_ALERT, ax=ax)
    
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color=C_TEXT, label_pos=0.5, ax=ax)
    
    ax.axis('off')
    save_fig('kruskal_prim_mst.png')

# ==========================================
# 10. TEMA 8: Dijkstra Shortest Path
# ==========================================
def gen_camino_minimo_dijkstra():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    G = nx.DiGraph()
    edges = [
        ('s', 'A', 4), ('s', 'B', 2), ('A', 'B', 1), ('A', 'C', 3),
        ('B', 'C', 5), ('B', 'D', 1), ('C', 't', 2), ('D', 't', 4),
        ('D', 'C', 2)
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
        
    pos = {
        's': (0, 1),
        'A': (1.2, 2),
        'B': (1.2, 0),
        'C': (3.0, 2),
        'D': (3.0, 0),
        't': (4.2, 1)
    }
    
    sp_edges = [('s', 'B'), ('B', 'D'), ('D', 'C'), ('C', 't')]
    sp_set = set(sp_edges)
    other_edges = [e for e in G.edges() if e not in sp_set]
    
    nx.draw_networkx_nodes(G, pos, node_color=C_BG, edgecolors=C_PRIMARY, node_size=600, linewidths=2, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=11, font_color=C_TEXT, font_weight='bold', ax=ax)
    
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, width=1.5, edge_color='#cbd5e1', arrowsize=15, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=sp_edges, width=3.5, edge_color=C_ALERT, arrowsize=20, ax=ax)
    
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color=C_TEXT, ax=ax)
    
    ax.axis('off')
    save_fig('camino_minimo_dijkstra.png')

# ==========================================
# 11. TEMA 9: Red de Flujo Máximo
# ==========================================
def gen_red_flujo_maximo():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    G = nx.DiGraph()
    edges = {
        ('s', 'A'): (10, 12),
        ('s', 'B'): (4, 4),
        ('A', 'B'): (2, 5),
        ('A', 't'): (8, 8),
        ('B', 't'): (6, 10)
    }
    
    for (u, v), (f, c) in edges.items():
        G.add_edge(u, v, flow=f, cap=c)
        
    pos = {
        's': (0, 1),
        'A': (1.5, 2),
        'B': (1.5, 0),
        't': (3.0, 1)
    }
    
    nx.draw_networkx_nodes(G, pos, node_color=C_BG, edgecolors=C_PRIMARY, node_size=600, linewidths=2, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=11, font_color=C_TEXT, font_weight='bold', ax=ax)
    
    sat_edges = [e for e, (f, c) in edges.items() if f == c]
    unsat_edges = [e for e, (f, c) in edges.items() if f < c]
    
    nx.draw_networkx_edges(G, pos, edgelist=unsat_edges, width=2.0, edge_color='#94a3b8', arrowsize=15, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=sat_edges, width=2.5, edge_color=C_SUCCESS, arrowsize=18, ax=ax)
    
    edge_labels = {(u, v): f"{d['flow']}/{d['cap']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color=C_TEXT, ax=ax)
    
    ax.axvline(x=0.85, color=C_ALERT, linestyle='dotted', lw=2.0)
    ax.text(0.75, 1.8, 'Corte $(S, T)$', color=C_ALERT, fontsize=11, fontweight='bold', ha='right')
    
    ax.axis('off')
    save_fig('red_flujo_maximo.png')

# ==========================================
# 12. TEMA 10: Bipartite Matching
# ==========================================
def gen_emparejamiento_bipartito():
    fig, ax = plt.subplots(figsize=(7, 5))
    
    G = nx.Graph()
    left = ['U1', 'U2', 'U3', 'U4']
    right = ['V1', 'V2', 'V3', 'V4']
    
    G.add_nodes_from(left, bipartite=0)
    G.add_nodes_from(right, bipartite=1)
    
    edges = [
        ('U1', 'V1'), ('U1', 'V2'), ('U2', 'V2'), ('U2', 'V3'),
        ('U3', 'V1'), ('U3', 'V3'), ('U3', 'V4'), ('U4', 'V3')
    ]
    G.add_edges_from(edges)
    
    pos = {}
    for i, node in enumerate(left):
        pos[node] = (0, 3 - i * 1.0)
    for i, node in enumerate(right):
        pos[node] = (2, 3 - i * 1.0)
        
    matching_edges = [('U1', 'V2'), ('U2', 'V3'), ('U3', 'V1')]
    matching_set = set(matching_edges)
    other_edges = [e for e in G.edges() if e not in matching_set and (e[1], e[0]) not in matching_set]
    
    nx.draw_networkx_nodes(G, pos, node_color=C_BG, edgecolors=C_PRIMARY, node_size=600, linewidths=2, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=11, font_color=C_TEXT, font_weight='bold', ax=ax)
    
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, width=1.5, edge_color='#cbd5e1', style='dashed', ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=matching_edges, width=3.5, edge_color=C_ALERT, ax=ax)
    
    ax.axis('off')
    save_fig('emparejamiento_bipartito.png')

# ==========================================
# 13. TEMA 11: TSP Tour
# ==========================================
def gen_tsp_ruta():
    fig, ax = plt.subplots(figsize=(7, 6))
    
    np.random.seed(24)
    points = np.random.rand(8, 2) * 10
    
    x = points[:, 0]
    y = points[:, 1]
    
    center = np.mean(points, axis=0)
    angles = np.arctan2(y - center[1], x - center[0])
    tour_idx = np.argsort(angles)
    tour_idx = list(tour_idx) + [tour_idx[0]]
    
    for i in range(len(tour_idx) - 1):
        idx1, idx2 = tour_idx[i], tour_idx[i+1]
        ax.plot([x[idx1], x[idx2]], [y[idx1], y[idx2]], color=C_PRIMARY, lw=2.5, zorder=2)
        ax.annotate(
            '', xy=(x[idx2], y[idx2]), xytext=(x[idx1], y[idx1]),
            arrowprops=dict(
                arrowstyle="-|>",
                color=C_PRIMARY,
                lw=2.5,
                mutation_scale=15,
                shrinkA=8,
                shrinkB=8
            )
        )
        
    ax.scatter(x, y, color=C_ALERT, s=120, edgecolors=C_TEXT, lw=1.5, zorder=5)
    for i, (px, py) in enumerate(points):
        ax.text(px + 0.25, py + 0.25, f'$C_{{{i+1}}}$', fontsize=11, fontweight='bold', color=C_TEXT, zorder=6)
        
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.axis('off')
    
    save_fig('tsp_ruta.png')

if __name__ == '__main__':
    print("Generating all illustrative figures...")
    gen_opt_1d_biseccion()
    gen_conjuntos_convexos()
    gen_epigrafo()
    gen_cono_direcciones()
    gen_condiciones_kkt()
    gen_region_factible_lp()
    gen_regresion_robusta()
    gen_puentes_konigsberg()
    gen_kruskal_prim_mst()
    gen_camino_minimo_dijkstra()
    gen_red_flujo_maximo()
    gen_emparejamiento_bipartito()
    gen_tsp_ruta()
    print("All figures generated successfully.")
