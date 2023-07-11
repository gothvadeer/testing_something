import numpy as np
import matplotlib.pyplot as grafico

x = np.outer(np.linspace(-2, 2, 100), np.ones(100))
y = x.copy().T
z = np.cos(x**3 + y**2)

fig = grafico.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, cmap='viridis')
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_title('Gráfico 3D')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
ax.view_init(elev=20, azim=-45)


grafico.show()

