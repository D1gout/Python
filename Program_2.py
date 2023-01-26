import math


def equation(a, b, c):
    if a == 0:
        if b != 0:
            x_l = c / -b
            return round(x_l, 3)
        else:
            return "b = 0"
    else:
        D = b * b - 4 * a * c
        if D >= 0:
            if D == 0:
                x = -b / 2 * a

                return round(x, 3)
            else:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)

                return round(x1, 3), round(x2, 3)
        else:
            return "Not real"

# error = "Y"
# while error == "Y":
#     s = list(map(float, input("Введите переменные (a | b | c) через пробел: ").split()))
#
#     a = s[0]
#     b = s[1]
#     c = s[2]
#
#     if a == 0:
#         if b != 0:
#             x_l = c / -b
#             print("Корень линейного уравнения = %.3f" % x_l)
#             error = "N"
#         else:
#             print("Ошибка - переменная (b) равна 0")
#             continue
#     else:
#         D = b * b - 4 * a * c
#         if D >= 0:
#             if D == 0:
#                 x = -b / 2 * a
#
#                 print("Корень уравнения = %.3f" % x)
#                 error = "N"
#             else:
#                 x1 = (-b + math.sqrt(D)) / (2 * a)
#                 x2 = (-b - math.sqrt(D)) / (2 * a)
#
#                 print("Первый корень уравнения = %.3f" % x1)
#                 print("Второй корень уравнения = %.3f" % x2)
#                 error = "N"
#         else:
#             print("Дискриминант меньше 0");
#             error = input("Что бы начать заново наберите Y, Что бы закончить N: \n");
#
#             if error == "Y":    # При ошибке все начинается с ввода чисел
#                 continue
#             if error == "N":    # Выход из приложения
#                 break
#
