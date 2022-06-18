import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    n = 5
    a = n
    t = np.ones((3 ** n, 3 ** n))
    start = 1
    step = 3
    size = 1

    while a > 0:
        for x in range(start, 3 ** n, step):
            for y in range(start, 3 ** n, step):
                for z in range(size):
                    for i in range(size):
                        t[x + z, y + i] = 0
        a -= 1
        start *= 3
        step *= 3
        size *= 3

    plt.matshow(t, cmap=plt.get_cmap('terrain'))
    plt.title("Sierpinski carpet")
    plt.axis("off")
    plt.show()
