import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

size = 100
data = {
    1: [[10, 0], [10, 0], None],
    2: [[0, 10], [10, 0], None],
    3: [[10, 0], [0, 10], None],
    4: [[0, 10], [0, 10], None]
}

for key, value in data.items():
    x = np.linspace(value[0][0], value[0][1], size)
    y = np.linspace(value[1][0], value[1][1], size)
    X, Y = np.meshgrid(x, y)
    data[key][2] = np.sqrt(X**2 + Y**2)


fig = plt.figure(figsize=(10, 10))
grid = ImageGrid(fig, 111,
                 nrows_ncols=(2, 2),  # creates 2x2 grid of Axes
                 axes_pad=0.1,  # pad between Axes in inch.
                 )

for ax, im, cmap in zip(grid, [data[1][2], data[2][2], data[3][2], data[4][2]], ['plasma'] * 4):
    ax.imshow(im, cmap)
    ax.axis('off')

plt.show()