from math import sqrt
import matplotlib.pyplot as plt


def sierpinski_triangle2(n, x, y, c):
    if n != 0:
        x1 = x
        y1 = y
        x2 = x + c
        y2 = y
        x3 = x + c / 2
        y3 = y + c * sqrt(3)/2
        x4 = (x1 + x2) / 2
        y4 = (y1 + y2) / 2
        x5 = (x2 + x3) / 2
        y5 = (y2 + y3) / 2
        x6 = (x1 + x3) / 2
        y6 = (y1 + y3) / 2

        plt.fill([x4, x5, x6], [y4, y5, y6], '#e6e9ed')

        sierpinski_triangle2(n - 1, x, y, c / 2)
        sierpinski_triangle2(n - 1, x6, y6, c / 2)
        sierpinski_triangle2(n - 1, x4, y4, c / 2)

    else:
        plt.fill([x, x + c, x + c / 2], [y, y, y + c * sqrt(3) / 2], '#2a7fad')


def sierpinski_triangle(n):
    sierpinski_triangle2(n, 0, 0, 10)

    plt.axis("equal")
    plt.axis("off")
    plt.title("Sierpinski triangle")
    plt.show()


if __name__ == "__main__":
    sierpinski_triangle(5)
