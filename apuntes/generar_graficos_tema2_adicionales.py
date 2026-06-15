import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

output_dir = r"C:\Users\vacek\Proyectos\OptimizacionAnalisisRedes\images"
os.makedirs(output_dir, exist_ok=True)

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

# 1. opt_1d_ejemplo.png
def gen_opt_1d_ejemplo():
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(0, 8, 300)
    f = lambda x: 0.25*x**4 - (13/3)*x**3 + 27*x**2 - 72*x + 1
    
    ax.plot(x, f(x), color=C_PRIMARY, lw=2.5, label=r'$f(x) = \frac{1}{4}x^4 - \frac{13}{3}x^3 + 27x^2 - 72x + 1$')
    
    # Shade interval [1, 4]
    ax.axvspan(1, 4, color=C_BG, alpha=0.5, label='Intervalo de búsqueda $[1, 4]$')
    
    # Highlight points
    ax.plot(1, f(1), 'o', color=C_TEXT, markersize=7)
    ax.text(1, f(1) + 4, r'$x=1$', ha='center', va='bottom', fontsize=10)
    
    ax.plot(4, f(4), 'o', color=C_TEXT, markersize=7)
    ax.text(4, f(4) - 4, r'$x=4$ (Máx local)', ha='center', va='top', fontsize=10)
    
    ax.plot(3, f(3), 'o', color=C_ALERT, markersize=8, zorder=5)
    ax.text(3, f(3) - 5, r'$x^*=3$ (Mín global)', ha='center', va='top', color=C_ALERT, fontweight='bold', fontsize=11)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    ax.set_xlabel('$x$', fontsize=11, color=C_TEXT)
    ax.set_ylabel('$f(x)$', fontsize=11, color=C_TEXT)
    ax.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none')
    
    save_fig('opt_1d_ejemplo.png')

# 2. coordenadas_ciclicas_ej1.png
def gen_coordenadas_ciclicas_ej1():
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Grid of points
    x = np.linspace(-1, 5, 200)
    y = np.linspace(-1, 5, 200)
    X, Y = np.meshgrid(x, y)
    Z = (X - 2)**2 + (Y - 1)**2
    
    # Plot contours
    contours = ax.contour(X, Y, Z, levels=[0.2, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0], colors='black', alpha=0.4, linewidths=1)
    ax.clabel(contours, inline=True, fontsize=8, fmt='%.1f')
    
    # Trajectory points
    x_coords = [0, 2, 2]
    y_coords = [0, 0, 1]
    
    # Plot steps as arrows
    for i in range(len(x_coords)-1):
        ax.annotate('', xy=(x_coords[i+1], y_coords[i+1]), xytext=(x_coords[i], y_coords[i]),
                    arrowprops=dict(arrowstyle="-|>", color=C_ALERT, lw=2.5, mutation_scale=15))
        
    ax.plot(x_coords, y_coords, 'o', color=C_ALERT, markersize=6)
    ax.plot(2, 1, '*', color=C_SUCCESS, markersize=12, label='Mínimo $(2,1)$')
    
    ax.text(0, -0.3, r'$x_0=(0,0)$', fontsize=10, ha='center', va='top')
    ax.text(2, -0.3, r'$x_1=(2,0)$', fontsize=10, ha='center', va='top')
    ax.text(2, 1.2, r'$x_2=(2,1)$', fontsize=10, ha='center', va='bottom', color=C_SUCCESS, fontweight='bold')
    
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    ax.set_xlabel('$x$', fontsize=11, color=C_TEXT)
    ax.set_ylabel('$y$', fontsize=11, color=C_TEXT)
    ax.set_title(r'Descenso por Coordenadas: $f(x,y) = (x-2)^2 + (y-1)^2$', fontsize=12, pad=15)
    ax.set_aspect('equal')
    
    save_fig('coordenadas_ciclicas_ej1.png')

# 3. coordenadas_ciclicas_ej2.png
def gen_coordenadas_ciclicas_ej2():
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Grid of points for f(x,y) = 8*x^2 + 3*x*y + 7*y^2 - 25*x + 31*y - 29
    x = np.linspace(-3, 7, 200)
    y = np.linspace(-7, 3, 200)
    X, Y = np.meshgrid(x, y)
    Z = 8*X**2 + 3*X*Y + 7*Y**2 - 25*X + 31*Y - 29
    
    # Plot contours
    contours = ax.contour(X, Y, Z, levels=[-50, -40, -20, 0, 50, 100, 200, 400], colors='black', alpha=0.4, linewidths=1)
    
    # Trajectory points for Coordinate Descent
    x_coords = [0, 25/16, 25/16, 7313/3584, 2.0405]
    y_coords = [0, 0, -571/224, -571/224, -2.6515]
    
    for i in range(len(x_coords)-1):
        ax.annotate('', xy=(x_coords[i+1], y_coords[i+1]), xytext=(x_coords[i], y_coords[i]),
                    arrowprops=dict(arrowstyle="-|>", color=C_ALERT, lw=2.5, mutation_scale=15))
        
    ax.plot(x_coords, y_coords, 'o', color=C_ALERT, markersize=5)
    
    # Optimum point
    opt_x, opt_y = 2.060, -2.656
    ax.plot(opt_x, opt_y, '*', color=C_SUCCESS, markersize=12, label='Óptimo $(2.06, -2.66)$')
    
    ax.text(0, 0.3, r'$x_0$', fontsize=10, ha='center', va='bottom')
    ax.text(1.56, 0.3, r'$x_1$', fontsize=10, ha='center', va='bottom')
    ax.text(1.3, -2.55, r'$x_2$', fontsize=10, ha='right', va='center')
    ax.text(2.2, -2.45, r'$x_3$', fontsize=10, ha='left', va='center')
    ax.text(opt_x + 0.2, opt_y - 0.2, r'$x^*=(2.06, -2.66)$', color=C_SUCCESS, fontweight='bold', fontsize=10, ha='left', va='top')
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-5, 1.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    ax.set_xlabel('$x$', fontsize=11, color=C_TEXT)
    ax.set_ylabel('$y$', fontsize=11, color=C_TEXT)
    ax.set_title(r'Coordenadas Cíclicas (Descenso por Coordenadas)', fontsize=12, pad=15)
    ax.set_aspect('equal')
    
    save_fig('coordenadas_ciclicas_ej2.png')

# 4. steepest_descent_ej.png
def gen_steepest_descent_ej():
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Grid of points
    x = np.linspace(-3, 7, 200)
    y = np.linspace(-7, 3, 200)
    X, Y = np.meshgrid(x, y)
    Z = 8*X**2 + 3*X*Y + 7*Y**2 - 25*X + 31*Y - 29
    
    # Plot contours
    contours = ax.contour(X, Y, Z, levels=[-50, -40, -20, 0, 50, 100, 200, 400], colors='black', alpha=0.4, linewidths=1)
    
    # Trajectory points for Steepest Descent
    x_coords = [0, 2.109, 2.054]
    y_coords = [0, -2.615, -2.660]
    
    for i in range(len(x_coords)-1):
        ax.annotate('', xy=(x_coords[i+1], y_coords[i+1]), xytext=(x_coords[i], y_coords[i]),
                    arrowprops=dict(arrowstyle="-|>", color=C_ALERT, lw=2.5, mutation_scale=15))
        
    ax.plot(x_coords, y_coords, 'o', color=C_ALERT, markersize=5)
    
    # Draw gradient vector at x0
    # grad f = (-25, 31), direction is (25, -31)
    ax.quiver(0, 0, -2.5, 3.1, scale=1, scale_units='xy', color=C_PRIMARY, width=0.007, zorder=10)
    ax.text(-2.5, 3.1, r'$\nabla f(x_0)$', color=C_PRIMARY, fontsize=10, ha='right', va='bottom')
    
    # Optimum point
    opt_x, opt_y = 2.060, -2.656
    ax.plot(opt_x, opt_y, '*', color=C_SUCCESS, markersize=12, label='Óptimo $(2.06, -2.66)$')
    
    ax.text(0.2, 0.2, r'$x_0$', fontsize=10, ha='left', va='bottom')
    ax.text(2.3, -2.6, r'$x_1$', fontsize=10, ha='left', va='center')
    ax.text(opt_x + 0.2, opt_y - 0.3, r'$x^*=(2.06, -2.66)$', color=C_SUCCESS, fontweight='bold', fontsize=10, ha='left', va='top')
    
    ax.set_xlim(-3, 5)
    ax.set_ylim(-5, 4.0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    ax.set_xlabel('$x$', fontsize=11, color=C_TEXT)
    ax.set_ylabel('$y$', fontsize=11, color=C_TEXT)
    ax.set_title(r'Método del Máximo Descenso (Steepest Descent)', fontsize=12, pad=15)
    ax.set_aspect('equal')
    
    save_fig('steepest_descent_ej.png')

# 5. cournot_monopolio.png
def gen_cournot_monopolio():
    fig, ax = plt.subplots(figsize=(7, 7))
    
    # Define points for the polygon (feasible region)
    # Vertices: (0,0), (0,8), (2,8), (9,1), (9,0)
    polygon_pts = np.array([[0, 0], [0, 8], [2, 8], [9, 1], [9, 0]])
    polygon = patches.Polygon(polygon_pts, closed=True, facecolor=C_BG, edgecolor=C_PRIMARY, lw=2, alpha=0.5, label='Región Factible')
    ax.add_patch(polygon)
    
    # Define grid
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='#cbd5e1')
    
    # Plot constraints
    q_vals = np.linspace(0.1, 10, 300)
    
    # Demand line Q = 10 - P => P = 10 - Q
    ax.plot(q_vals, 10 - q_vals, color='#475569', lw=1.5, linestyle=':', label='Curva de Demanda $P = 10 - Q$')
    
    # Isobenefit curves: P = 3 + (B + 1)/Q
    # For B = 5
    ax.plot(q_vals[q_vals > 0.5], 3 + 6 / q_vals[q_vals > 0.5], color='#ef4444', lw=1, linestyle='--', alpha=0.5)
    ax.text(8.5, 3 + 6/8.5 + 0.1, '$B = 5$', color='#ef4444', fontsize=9, ha='left')
    
    # For B = 8
    ax.plot(q_vals[q_vals > 0.8], 3 + 9 / q_vals[q_vals > 0.8], color='#ef4444', lw=1, linestyle='--', alpha=0.7)
    ax.text(8.5, 3 + 9/8.5 + 0.1, '$B = 8$', color='#ef4444', fontsize=9, ha='left')
    
    # For B = 11.25 (optimum)
    ax.plot(q_vals[q_vals > 1.2], 3 + 12.25 / q_vals[q_vals > 1.2], color=C_ALERT, lw=2.5, label='Isobeneficio óptimo $B = 11.25$')
    
    # Highlight optimal point
    opt_q, opt_p = 3.5, 6.5
    ax.plot(opt_q, opt_p, 'o', color=C_ALERT, markersize=8, zorder=10)
    ax.annotate(r'$x^* = (3.5, 6.5)$' + '\n' + r'$B^* = 11.25$', xy=(opt_q, opt_p), xytext=(opt_q + 0.5, opt_p + 0.5),
                arrowprops=dict(facecolor=C_TEXT, arrowstyle='->'), fontweight='bold', color=C_ALERT, fontsize=10)
    
    # Set limits
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 10.5)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_TEXT_MUTED)
    ax.spines['bottom'].set_color(C_TEXT_MUTED)
    
    ax.set_xlabel('$Q$ (cantidad)', fontsize=11, color=C_TEXT)
    ax.set_ylabel('$P$ (precio)', fontsize=11, color=C_TEXT)
    ax.set_title('Monopolio de Cournot: Región Factible e Isobeneficios', fontsize=12, pad=15)
    ax.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none')
    ax.set_aspect('equal')
    
    save_fig('cournot_monopolio.png')

if __name__ == '__main__':
    print("Generating additional figures for Tema 2...")
    gen_opt_1d_ejemplo()
    gen_coordenadas_ciclicas_ej1()
    gen_coordenadas_ciclicas_ej2()
    gen_steepest_descent_ej()
    gen_cournot_monopolio()
    print("All additional figures generated successfully.")
