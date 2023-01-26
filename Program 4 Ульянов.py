import math
import matplotlib.pyplot as plt
import numpy as np


class Primitive:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def func1(x):
        return (math.cos(x)) / (math.e ** x)

    @staticmethod
    def func2(x):
        return 5 * (x ** 2) - x + 2

    def prim_func1(self):
        prim = (-1 / 2 * (math.e ** -self.b) * (math.cos(self.b) -
                                                math.sin(self.b))) - (
                       -1 / 2 * (math.e ** -self.a) * (math.cos(self.a) -
                                                       math.sin(self.a)))
        return prim

    def prim_func2(self):
        prim = (5 / 3 * (self.b ** 3) - 1 / 2 * (self.b ** 2) + 2 * self.b) - (
                5 / 3 * (self.a ** 3) - 1 / 2 * (self.a ** 2) + 2 * self.a)
        return prim


class Operation:

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def sims(self, num):
        f = 0
        if num == 1:
            f = Primitive.func1
        elif num == 2:
            f = Primitive.func2

        h = (self.b - self.a) / self.n
        x = self.a
        rect = 0.0
        while x < self.b:
            rect += (f(x - h) + 3 * f(
                (2 * (x - h) + x) / 3) + 3 * f(
                ((x - h) + 2 * x) / 3) + f(x)) / 8 * h

            x += h

        return rect

    def rect_p(self, num):
        f = 0
        if num == 1:
            f = Primitive.func1
        elif num == 2:
            f = Primitive.func2

        h = (self.b - self.a) / self.n
        x = self.a + h
        rect = 0.0
        while x < self.b:
            rect += f(x)

            x += h

        rect = h * rect

        return rect

    def rect_s(self, num):
        f = 0
        if num == 1:
            f = Primitive.func1
        elif num == 2:
            f = Primitive.func2

        h = (self.b - self.a) / self.n
        x = self.a + h
        rect = 0.0
        while x < self.b:
            rect += (f(x) + h/2)

            x += h

        rect = h * rect

        return rect


print("Приближенное вычисление интеграла 1-й функции")
print("f(x) = cos(x) / e^x")
k1 = 1
a1 = 0
b1 = 0
n1 = 0
while k1 == 1:
    try:
        a1 = float(input("Нижняя граница интервала a: "))
        b1 = float(input("Верхняя граница интервала b: "))
        n1 = float(input("Количество шагов: "))
        k1 = 0
    except:
        print("Неверный ввод данных")
        k1 = 1

f = Operation(a1, b1, n1)
f_default = Primitive(a1, b1)
print("Результаты численного интегрирования")
print(f"Функция 1: f(x) = cos(x) / e^x;"
      f" a = {a1}; b = {b1}; шаг = {(b1 - a1) / n1}")

print(f"Аналитическое значение интеграла: {f_default.prim_func1():.10f}")
print(f"Метод правых прямоугольников:     "
      f"{f.rect_p(1):.10f}, "
      f"погрешность: {abs(f.rect_p(1) - f_default.prim_func1()):.10f}")

print(f"Метод средних прямоугольников:    "
      f"{f.rect_s(1):.10f}, "
      f"погрешность: {abs(f.rect_s(1) - f_default.prim_func1()):.10f}")

print(f"Метод Симпсона 3/8:               "
      f"{f.sims(1):.10f}, "
      f"погрешность: {abs(f.sims(1) - f_default.prim_func1()):.10f}")

print("-" * 100)

print("Приближенное вычисление интеграла 2-й функции")
print("f(x) = 5x^2 - x + 2")
k2 = 1
a2 = 0
b2 = 0
n2 = 0
while k2 == 1:
    try:
        a2 = float(input("Нижняя граница интервала a: "))
        b2 = float(input("Верхняя граница интервала b: "))
        n2 = float(input("Количество шагов: "))
        k2 = 0
    except:
        print("Неверный ввод данных")
        k2 = 1

f = Operation(a2, b2, n2)
f_default = Primitive(a2, b2)
print("Результаты численного интегрирования")
print(f"Функция 2: f(x) = 5x^2 - x + 2;"
      f" a = {a2}; b = {b2}; шаг = {(b2 - a2) / n2}")

print(f"Аналитическое значение интеграла: {f_default.prim_func2():.10f}")
print(f"Метод правых прямоугольников:     "
      f"{f.rect_p(2):.10f}, "
      f"погрешность: {abs(f.rect_p(2) - f_default.prim_func2()):.10f}")

print(f"Метод средних прямоугольников:    "
      f"{f.rect_s(2):.10f}, "
      f"погрешность: {abs(f.rect_s(2) - f_default.prim_func2()):.10f}")

print(f"Метод Симпсона 3/8:               "
      f"{f.sims(2):.10f}, "
      f"погрешность: {abs(f.sims(2) - f_default.prim_func2()):.10f}")

grid1 = plt.grid(True)

x1 = np.arange(0, 20, (20 - 0) / 100)
x2 = np.arange(a1, b1, (b1 - a1) / n1)
x1_1 = np.cos(x1) / np.e ** x1
x2_1 = np.cos(x2) / np.e ** x2

plt.plot(x1, x1_1, x2, x2_1)
plt.fill_between(x2, x2_1, color='red', alpha=.2)
plt.title('cos(x) / e^x')

x3 = np.arange(0, 20, (20 - 0) / 100)
x4 = np.arange(a2, b2, (b2 - a2) / n2)
x3_1 = 5 * (x3 ** 2) - x3 + 2
x4_1 = 5 * (x4 ** 2) - x4 + 2

plt.subplots()
grid2 = plt.grid(True)
plt.plot(x3, x3_1, x4, x4_1)
plt.fill_between(x4, x4_1, color='green', alpha=.2)
plt.title('5x^2 - x + 2')

plt.show()
