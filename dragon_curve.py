from math import sqrt, cos, sin, pi
import numpy as np
import random
import matplotlib.pyplot as plt


def f1(x, y):
    return (1 / sqrt(2)) * np.array([[cos(pi/4), -sin(pi/4)], [sin(pi/4), cos(pi/4)]]).dot(np.array([x, y]))


def f2(x, y):
    return (1 / sqrt(2)) * np.array([[cos(3*pi/4), -sin(3*pi/4)], [sin(3*pi/4), cos(3*pi/4)]]).dot(np.array([x, y])) + np.array([1, 0])

def make_fractal():
    n = 50000
    x, y = [0], [0]
    for _ in range(n):
        r = random.random()
        if r <= 0.5:
            dot = f1(x[-1], y[-1])
        else:
            dot = f2(x[-1], y[-1])
        x.append(dot[0])
        y.append(dot[1])
    plt.plot(x, y, '.', markersize=0.8, color='#D6006E')
    plt.title("Dragon curve")
    plt.tight_layout()
    plt.axis('off')
    plt.show()



if __name__ == "__main__":
    make_fractal()