import numpy as np
import matplotlib.pyplot as plt


def julia_quadratic(zx, zy, cx, cy, threshold):
    z = complex(zx, zy)
    c = complex(cx, cy)

    for i in range(threshold):
        z = z ** 2 + c
        if abs(z) > 4.:
            return i

    return threshold - 1


def make_fractal(iterations):
    x_start, y_start = -2, -2
    width, height = 4, 4
    density_per_unit = 100

    re = np.linspace(x_start, x_start + width, width * density_per_unit)
    im = np.linspace(y_start, y_start + height, height * density_per_unit)
    x = np.empty((len(re), len(im)))
    r = 0.7885
    a = 2 * np.pi / 4.
    cx, cy = r * np.cos(a), r * np.sin(a)

    for i in range(len(re)):
        for j in range(len(im)):
            x[i, j] = julia_quadratic(zx=re[i], zy=im[j], cx=cx, cy=cy, threshold=iterations)

    plt.figure(figsize=(10, 10))
    plt.axes().imshow(x.T, cmap='inferno')
    plt.title("Julia set")
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    make_fractal(30)