from math import sqrt
import matplotlib.pyplot as plt


def koch_curve(x, x1, y1, x2, y2):
    if x != 0:
        x3 = x1 + (x2 - x1) / 3
        y3 = y1 + (y2 - y1) / 3
        x4 = x1 + 2 * (x2 - x1) / 3
        y4 = y1 + 2 * (y2 - y1) / 3
        x5 = (x3 + x4) / 2 - (y4 - y3) * sqrt(3) / 2
        y5 = (y3 + y4) / 2 + (x4 - x3) * sqrt(3) / 2

        koch_curve(x - 1, x1, y1, x3, y3)
        koch_curve(x - 1, x3, y3, x5, y5)
        koch_curve(x - 1, x5, y5, x4, y4)
        koch_curve(x - 1, x4, y4, x2, y2)
    else:
        plt.plot([x1, x2], [y1, y2], '#8abef2')


def koch_snowflake(x):
    x1 = 0
    y1 = 0
    x2 = 1 / 2
    y2 = sqrt(0.75)
    x3 = 1
    y3 = 0

    koch_curve(x, x1, y1, x2, y2)
    koch_curve(x, x2, y2, x3, y3)
    koch_curve(x, x3, y3, x1, y1)

    plt.axis("equal")
    plt.axis("off")
    plt.title("Koch snowflake")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    koch_snowflake(4)
