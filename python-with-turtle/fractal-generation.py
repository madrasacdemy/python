import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

img = np.zeros((height, width))
for x in range(width):
    for y in range(height):
        zx = xmin + (xmax - xmin) * x / (width - 1)
        zy = ymin + (ymax - ymin) * y / (height - 1)
        img[y, x] = mandelbrot(complex(zx, zy), 100)

plt.imshow(img, cmap='twilight_shifted', extent=(xmin, xmax, ymin, ymax))
plt.axis('off')
plt.show()