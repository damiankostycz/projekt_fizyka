import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    n = 3

    t1 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

    for i in range(1, n + 1):
        t2 = np.ones((3 ** i, 3 ** i))
        t3 = np.hstack((t2, t1, t2))
        t4 = np.hstack((t1, t2, t1))
        t1 = np.vstack((t4, t3, t4))

    plt.matshow(t1, cmap='terrain')
    plt.title("Viscek fractal")
    plt.axis("off")
    plt.show()
