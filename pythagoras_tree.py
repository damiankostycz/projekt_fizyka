from math import sin, cos, pi
import matplotlib.pyplot as plt


def pythagoras_tree(x, y, length, beta, angle2, order2, counter):
    l1 = length * sin(beta)
    l2 = length * cos(beta)

    t1 = [x]
    t2 = [y]

    x1 = x + l1
    y1 = y - l2
    t1.append(x1)
    t2.append(y1)

    x2 = x + l1 - l2
    y2 = y - l2 - l1
    t1.append(x2)
    t2.append(y2)

    x3 = x - l2
    y3 = y - l1
    t1.append(x3)
    t2.append(y3)

    x4 = x - l2 + length * cos(angle2) * sin(beta - angle2)
    y4 = y - l1 - length * cos(angle2) * cos(beta - angle2)

    plt.fill(t1, t2, color=(counter / (color + 5), counter / color, counter / (color + 3)))
    plt.axis('equal')

    if order2 > 0:
        pythagoras_tree(x4, y4, length * sin(angle2), beta - angle2 + pi / 2, angle2, order2 - 1, counter + 1)

        pythagoras_tree(x3, y3, length * cos(angle2), beta - angle2, angle2, order2 - 1, counter + 1)


if __name__ == "__main__":
    a = 0
    b = 0
    c = 1
    order = 9
    angle = pi / 3
    alpha = -pi / 2
    color = order + 1

    pythagoras_tree(a - 1, b - 1, c, -pi / 2, angle * 7 / 12, order, 1)

    plt.title("Pythagoras tree")
    plt.tight_layout()
    plt.axis("off")
    plt.show()
