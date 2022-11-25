import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math
import random

MIN_RADIUS = 0.1
MIN_Q = 1
ARENA_SIZE = 20.0
STEP_ARENA = ARENA_SIZE / 30.0


class Point:
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q


def E(points, x, y):
    Ex = 0.0
    Ey = 0.0
    for i in points:
        r = math.sqrt((x - i.x) ** 2 + (y - i.y) ** 2)
        Ex += i.q * (x - i.x) / r ** 3
        Ey += i.q * (y - i.y) / r ** 3
    E = (Ex ** 2 + Ey ** 2)
    return E


def go_E(points):
    ans = []
    for i in np.arange(-ARENA_SIZE, ARENA_SIZE, STEP_ARENA):
        for j in np.arange(-ARENA_SIZE, ARENA_SIZE, STEP_ARENA):
            ok = True
            for p in points:
                r = math.sqrt((i - p.x) ** 2 + (j - p.y) ** 2)
                if r < MIN_RADIUS:
                    ok = False
            if ok:
                ans.append([i, j, E(points, i, j)])
    return ans

def plot_points(points):
    print("go_E starting...")
    p = go_E(points)

    # sort by E
    print("sorting...")
    p.sort(key=lambda x: x[2])

    # add points
    print("adding points...")
    color_x = [i[0] for i in p]
    color_y = [i[1] for i in p]
    color_z = [i for i in range(len(p))]
    plt.scatter(color_x, color_y, c=color_z, cmap=cm.Reds, s=1)

    plt.xlim(-ARENA_SIZE, ARENA_SIZE)
    plt.ylim(-ARENA_SIZE, ARENA_SIZE)

    print("showing...")
    for i in points:
        if i.q > 0:
            plt.scatter(i.x, i.y, color='black', s=15)
        else:
            plt.scatter(i.x, i.y, color='green', s=15)

    plt.ion()
    while True:
        plt.show()
        plt.pause(0.1)
        # fast get and print mouse coordinates
        print("E = ", E(points, plt.ginput(1, timeout=0)[0][0], plt.ginput(1, timeout=0)[0][1]), "V/m")


def main():
    # random points
    given_points = []
    for i in range(15):
        given_points.append(Point(random.randrange(-ARENA_SIZE, ARENA_SIZE), random.randrange(-ARENA_SIZE, ARENA_SIZE),
                                  (-1) ** i * MIN_Q))
    plot_points(given_points)


if __name__ == '__main__':
    main()
