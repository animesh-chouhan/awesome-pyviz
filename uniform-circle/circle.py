# https://leetcode.com/problems/generate-random-point-in-a-circle/description/

import math
import random
import matplotlib.pyplot as plt
import numpy as np


# https://matplotlib.org/stable/plot_types/basic/plot.html
plt.style.use("_mpl-gallery")


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self, *args) -> list[float]:
        # Write your code here
        rand_y = random.uniform(-self.radius, self.radius)
        rand_x = random.uniform(-self.radius, self.radius)
        x = self.x_center + rand_x
        y = self.y_center + rand_y
        return [x, y]

    def plot(self, description):
        # Generate points
        iterations = 20000
        x = []
        y = []
        for i in range(iterations):
            p = self.randPoint(self)
            x.append(p[0])
            y.append(p[1])

        r = [math.sqrt(a**2 + b**2) for a, b in zip(x, y)]

        # Plot
        s = [1] * len(x)
        fig, ax = plt.subplots(1, 2, layout="constrained", figsize=(14, 6))
        fig.set_constrained_layout_pads(w_pad=0.8, h_pad=0.9)
        ax[0].scatter(x, y, s, color="black")

        lim = (-radius * 1.2, radius * 1.2)
        ax[0].set(xlim=lim, xticks=np.arange(*lim), ylim=lim, yticks=np.arange(*lim))
        ax[0].set(aspect=1)

        circle = plt.Circle((0, 0), radius, color="black", fill=False)
        ax[0].add_patch(circle)

        binwidth = 0.1
        lim = (int(np.max(r) / binwidth) + 1) * binwidth
        bins = np.arange(-lim, lim + binwidth, binwidth)
        ax[1].hist(r, bins=bins, density=False, edgecolor="white", color="black")
        ax[1].set(
            xlim=(0, radius),
            xticks=np.arange(0, radius + binwidth, binwidth * 2),
            ylim=(0, 1000),
            yticks=np.linspace(0, 1000, 11),
            xlabel="Radius",
            ylabel="No. of Points",
        )
        ax[1].set_aspect(np.diff(ax[1].get_xlim())[0] / np.diff(ax[1].get_ylim())[0])

        fig.suptitle(
            description, y=0.04, ha="center", fontsize="xx-large", fontweight="bold"
        )
        mng = plt.get_current_fig_manager()
        mng.resize(1920, 1080)
        plt.show()


radius = 5
s = Solution(radius, 0, 0)
s.plot("• Random square")


# wrong
# def randPoint(self) -> list[float]:
#     r = random.uniform(0, self.radius)
#     theta = 2 * math.pi * random.uniform(0, 1)
#     x = self.x_center + r * math.cos(theta)
#     y = self.y_center + r * math.sin(theta)
#     return [x, y]


# s.randPoint = randPoint
# s.plot("• Naive approach")


# square
# def randPoint(self) -> list[float]:
#     while True:
#         rand_y = random.uniform(-self.radius, self.radius)
#         rand_x = random.uniform(-self.radius, self.radius)
#         if rand_x**2 + rand_y**2 <= self.radius**2:
#             break
#     x = self.x_center + rand_x
#     y = self.y_center + rand_y
#     return [x, y]


# s.randPoint = randPoint
# s.plot("• Random constrained approach")


# sqrt
# def randPoint(self) -> list[float]:
#     theta = random.uniform(0, 2 * math.pi)
#     R = math.sqrt(random.uniform(0, self.radius**2))
#     return [
#         self.x_center + R * math.cos(theta),
#         self.y_center + R * math.sin(theta),
#     ]


# s.randPoint = randPoint
# s.plot("• Probabilistic distribution approach")
