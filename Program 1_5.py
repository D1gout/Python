import math
import random

import matplotlib.patches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

axes = plt.gca()
axes.grid()


class Drawing:

    def __init__(self, cor_x, cor_y, x_wight, y_wight, count):
        self.cor_x = cor_x
        self.cor_y = cor_y
        self.x_wight = x_wight
        self.y_wight = y_wight
        self.count = count

    def drawRect(self):
        axes = plt.gca()

        rect_back = matplotlib.patches.Rectangle(
            (self.cor_x - (self.x_wight / 2),
             self.cor_y - (self.y_wight / 2)),
            self.x_wight, self.y_wight,
            color="yellow",
            alpha=.1)

        rect_front = matplotlib.patches.Rectangle(
            (self.cor_x - (self.x_wight / 2),
             self.cor_y - (self.y_wight / 2)),
            self.x_wight, self.y_wight,
            color="black",
            linewidth=1.5,
            fill=None)

        axes.add_patch(rect_back)
        axes.add_patch(rect_front)

    def drawDots(self):
        axes = plt.gca()

        xlo, xhi = self.cor_x - (self.x_wight / 2), self.cor_x + (
                self.x_wight / 2)
        ylo, yhi = self.cor_y - (self.y_wight / 2), self.cor_y + (
                self.y_wight / 2)

        sum_dots = 0

        for points in range(self.count + 1):
            rand_x = random.uniform(xlo, xhi)
            rand_y = random.uniform(ylo, yhi)

            line1_y = rand_x + 3                        # line 1
            line2_y = -0.5 * rand_x                     # line 2

            check = -60 - (rand_x ** 2) + 16 * rand_x   # формула
            circle_y = math.sqrt(abs(check)) - 2        # circle 1

            if -4 <= rand_x <= -2:
                if rand_y <= line1_y:
                    axes.scatter(rand_x, rand_y, s=7, marker='x', color='blue')
                    sum_dots += 1
                else:
                    axes.scatter(rand_x, rand_y, s=7, marker='x', color='red')

            if -2 <= rand_x <= 4:
                if rand_y <= line2_y:
                    axes.scatter(rand_x, rand_y, s=7, marker='x', color='blue')
                    sum_dots += 1
                else:
                    axes.scatter(rand_x, rand_y, s=7, marker='x', color='red')

            if 4 <= rand_x <= 6:
                if rand_y <= -2:
                    axes.scatter(rand_x, rand_y, s=7, marker='x', color='blue')
                    sum_dots += 1
                else:
                    axes.scatter(rand_x, rand_y, s=7, marker='x', color='red')

            if 6 <= rand_x <= 10:
                if rand_y <= circle_y:
                    axes.scatter(rand_x, rand_y, s=7, marker='x', color='blue')
                    sum_dots += 1
                else:
                    axes.scatter(rand_x, rand_y, s=7, marker='x', color='red')

        print(f"Площадь ограниченной области = "
              f"{self.x_wight * self.y_wight * (sum_dots / self.count)}")

    @staticmethod
    def drawLine():
        axes = plt.gca()

        stepx = np.arange(-4, 11, 1)
        stepy = np.arange(-5, 6, 1)
        plt.axis([-5, 11, -6, 6])
        plt.xticks(stepx)
        plt.yticks(stepy)
        axes.spines[['left', 'bottom']].set_position(('data', 0))
        axes.spines['top'].set_visible(False)
        axes.spines['right'].set_visible(False)

        line1 = Line2D([-4, -3, -2], [-1, 0, 1], color='black')
        line2 = Line2D([-2, 0, 4], [1, 0, -2], color='black')
        line3 = Line2D([4, 6], [-2, -2], color='black')
        line4 = Line2D([-4, -3, -2], [-1, 0, 1], color='black')
        axes.add_line(line1)
        axes.add_line(line2)
        axes.add_line(line3)
        axes.add_line(line4)

    @staticmethod
    def drawArc():
        axes = plt.gca()

        arc = matplotlib.patches.Arc((8, -2), 4, 4, theta1=360, theta2=180,
                                     color='black', linewidth=1.5)

        axes.add_patch(arc)


x = float(input("Введите координаты x: "))
y = float(input("Введите координаты y: "))
wight_x = float(input("Введите размер области x: "))
wight_y = float(input("Введите размер области y: "))
n = int(input("Введите количество точек: "))

fig = Drawing(x, y, wight_x, wight_y, n)

fig.drawLine()
fig.drawArc()
fig.drawRect()
fig.drawDots()

print(f"Площадь ограничивающей области = {wight_x * wight_y}")

plt.show()
