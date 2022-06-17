import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def matrixes():
    f1 = lambda x, y: (0., 0.16*y)
    f2 = lambda x, y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
    f3 = lambda x, y: (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
    f4 = lambda x, y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
    fs = [f1, f2, f3, f4]
    return fs


def make_fractal():
    iteraions = 50000
    width, height = 300, 300
    aimg = np.zeros((width, height))
    x, y = 0, 0
    for i in range(iteraions):
        f = np.random.choice(matrixes(), p=[0.01, 0.85, 0.07, 0.07])
        x, y = f(x, y)
        ix, iy = int(width / 2 + x * width / 10), int(y * height / 12)
        aimg[iy, ix] = 1

    plt.imshow(aimg[::-1, :], cmap=cm.Greens)
    plt.title("Barnsley fern")
    plt.axis('off')
    plt.show()



if __name__ == "__main__":
    make_fractal()