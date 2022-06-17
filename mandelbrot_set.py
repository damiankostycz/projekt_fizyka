import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, z):
    iterations = 150
    count = 0
    for a in range(iterations):
        z = z ** 2 + c
        count += 1
        if (abs(z) > 4):
            break
    return count


def mandelbrot_set():
    rows = 800
    cols = 1000
    x = np.linspace(-2, 1, cols)
    y = np.linspace(-1, 1, rows)
    m = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            z = complex(0, 0)
            count = mandelbrot(c, z)
            m[i, j] = count

    plt.imshow(m.T, cmap="magma")
    plt.title("Mandelbrot set")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    mandelbrot_set()
