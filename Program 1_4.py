import math
import matplotlib.pyplot as plt
import numpy as np


class Primitive:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def func1(x):
        return (5 * math.sin(x)) / (math.e ** (x / 5))

    @staticmethod
    def func2(x):
        return 7 * (x ** 2) + x ** (1 / 3)

    def prim_func1(self):
        prim = (-1 * ((25 * math.sin(self.b) + 125 * math.cos(self.b)) / (
                26 * math.e ** (self.b / 5)))) - (-1 * (
                (25 * math.sin(self.a) + 125 * math.cos(self.a)) / (
                26 * math.e ** (self.a / 5))))
        return prim

    def prim_func2(self):
        prim = (7 * (self.b ** 3)) / 3 + (3 * (self.b ** (4 / 3))) / 4 - (
                7 * (self.a ** 3)) / 3 + (3 * (self.a ** (4 / 3))) / 4
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

    def rect(self, num):
        f = 0
        if num == 1:
            f = Primitive.func1
        elif num == 2:
            f = Primitive.func2

        h = (self.b - self.a) / self.n
        x = self.a
        rect = 0.0
        while x < self.b:
            rect += f(x)
            x += h

        rect = h * rect

        return rect

    def trap(self, num):
        f = 0
        if num == 1:
            f = Primitive.func1
        elif num == 2:
            f = Primitive.func2

        h = (self.b - self.a) / self.n
        x = self.a
        rect = 0.0
        while x < self.b:
            rect += ((f(x) + f(x - h)) / 2) * h
            x += h

        return rect


print("Приближенное вычисление интеграла 1-й функции")
print("f(x) = 5 * sin(x) / e^(x/5)")
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
        print("Не верный ввод данных")
        k1 = 1

f = Operation(a1, b1, n1)
f_default = Primitive(a1, b1)
print("Результаты численного интегрирования")
print(f"Функция 1: f(x) = 5 * sin(x) / e^(x/5);"
      f" a = {a1}; b = {b1}; шаг = {(b1 - a1) / n1}")

print(f"Аналитическое значение интеграла: {f_default.prim_func1():.10f}")
print(f"Метод левых прямоугольников:      "
      f"{f.rect(1):.10f}, "
      f"погрешность: {abs(f.rect(1) - f_default.prim_func1()):.10f}")

print(f"Метод трапеций:                   "
      f"{f.trap(1):.10f}, "
      f"погрешность: {abs(f.trap(1) - f_default.prim_func1()):.10f}")

print(f"Метод Симпсона 3/8:               "
      f"{f.sims(1):.10f}, "
      f"погрешность: {abs(f.sims(1) - f_default.prim_func1()):.10f}")

print("-" * 100)

print("Приближенное вычисление интеграла 2-й функции")
print("f(x) = 7x^2 + x^1/3")
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
        print("Не верный ввод данных")
        k2 = 1

f = Operation(a2, b2, n2)
f_default = Primitive(a2, b2)
print("Результаты численного интегрирования")
print(f"Функция 2: f(x) = 7x^2 + x^1/3;"
      f" a = {a2}; b = {b2}; шаг = {(b2 - a2) / n2}")

print(f"Аналитическое значение интеграла: {f_default.prim_func2():.10f}")
print(f"Метод левых прямоугольников:      "
      f"{f.rect(2):.10f}, "
      f"погрешность: {abs(f.rect(2) - f_default.prim_func2()):.10f}")

print(f"Метод трапеций:                   "
      f"{f.trap(2):.10f}, "
      f"погрешность: {abs(f.trap(2) - f_default.prim_func2()):.10f}")
print("Из-за x^1/3 появляются комплексные корни")
print(f"Метод Симпсона 3/8:               "
      f"{f.sims(2):.10f}, "
      f"погрешность: {abs(f.sims(2) - f_default.prim_func2()):.10f}")
print("Из-за x^1/3 появляются комплексные корни")
grid1 = plt.grid(True)

x1 = np.arange(0, 20, (20 - 0) / 100)
x2 = np.arange(a1, b1, (b1 - a1) / n1)
x1_1 = (5 * np.sin(x1)) / (np.e ** (x1 / 5))
x2_1 = (5 * np.sin(x2)) / (np.e ** (x2 / 5))

plt.plot(x1, x1_1, x2, x2_1)
plt.fill_between(x2, x2_1, color='red', alpha=.2)
plt.title('5 * sin(x) / e^x/5')

x3 = np.arange(0, 20, (20 - 0) / 100)
x4 = np.arange(a2, b2, (b2 - a2) / n2)
x3_1 = 7 * (x3 ** 2) + x3 ** (1 / 3)
x4_1 = 7 * (x4 ** 2) + x4 ** (1 / 3)

plt.subplots()
grid2 = plt.grid(True)
plt.plot(x3, x3_1, x4, x4_1)
plt.fill_between(x4, x4_1, color='green', alpha=.2)
plt.title('7x^2 + x^1/3')

plt.show()
