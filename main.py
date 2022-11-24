import matplotlib.pyplot as plt
import numpy as np
import math
import random

MIN_RADIUS = 0.002
MIN_Q = 0.01
ARENA_SIZE = 15.0
STEP_ARENA = 0.05

class Point:
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q


def E(point, x, y):
    Ex = 0
    Ey = 0
    for i in point:
        r = (x - i.x) ** 2 + (y - i.y) ** 2
        if r > 0:
            Ex += i.q * (x - i.x) / r
            Ey += i.q * (y - i.y) / r
    return Ex, Ey


def go_E(point, coordinates):
    ansX = []
    ansY = []
    ansEX = []
    ansEY = []
    for (i, j) in coordinates:
        Ex, Ey = E(point, i, j)
        ansX.append(i)
        ansY.append(j)
        ansEX.append(Ex)
        ansEY.append(Ey)
    return ansX, ansY, ansEX, ansEY

def dotes(points):
    v = []
    for i in np.arange(-ARENA_SIZE, ARENA_SIZE, STEP_ARENA):
        for j in np.arange(-ARENA_SIZE, ARENA_SIZE, STEP_ARENA):
            flag = True
            for k in points:
                r = (i - k.x) ** 2 + (j - k.y) ** 2
                if r < MIN_RADIUS:
                   flag = False
            if flag:
                v.append((i, j))
    return v

def plot_points(points):
    x = [p.x for p in points]
    y = [p.y for p in points]

    v = dotes(points)

    q_x, q_y, q_Ex, q_Ey = go_E(points, v)

    plt.quiver(q_x, q_y, q_Ex, q_Ey, color='b', scale=1, width=0.001)

    plt.xlim(-ARENA_SIZE, ARENA_SIZE)
    plt.ylim(-ARENA_SIZE, ARENA_SIZE)

    plt.plot(x, y, 'ro', markersize=2, color = 'r')

    plt.show()


def main():
    # random points
    given_points = []
    for i in range(2):
        given_points.append(Point(random.randrange(-ARENA_SIZE, ARENA_SIZE), random.randrange(-ARENA_SIZE, ARENA_SIZE), (-1) ** i * MIN_Q))
    plot_points(given_points)


if __name__ == '__main__':
    main()
