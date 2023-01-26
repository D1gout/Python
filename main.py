import random

print("Аракелян Эрик Размикович \nРабота №3 \nВариант №5")
columns = int(input("Кол-во столбцов: "))
rows = int(input("Кол-во строк: "))
rand_min = int(input("Макс: "))
rand_max = int(input("Мин: "))

print("")

print("Матрица:")
matrix_f = []
for i in range(columns):
    row = []
    for j in range(rows):
        rn = rand_min + (rand_max - rand_min) * random.random()
        row.append(rn)
        matrix_f.append(row)

text = ''
for i in range(rows):
    for j in range(columns):
        text += ('{:.2f}'.format(matrix_f[j][i])) + " "
    text += "\n"
print(text)


def transporent():
    text = ''
    for j in range(columns):
        for i in range(rows):
            text += ('{:.2f}'.format(matrix_f[j][i])) + " "
        text += "\n"
    return text


def summing():
    sum = 0
    text = ''
    for i in range(rows):
        for j in range(columns):
            text += ('{:.2f}'.format(matrix_f[j][i])) + " "
            sum += float(matrix_f[j][i])
        text += "- Сумма " + ('{:.2f}'.format(sum))
        sum = 0
        text += "\n"
    return text


def max_element():
    dM = 0
    text = ''
    for i in range(rows):
        for j in range(columns):
            if i == j:
                if float(matrix_f[j][i]) > dM:
                    dM = float(matrix_f[j][i])

        text = ('{:.2f}'.format(dM))
    return text


print("Транспонирование матрицы:")

print(transporent())

print("Сумма по строкам")

print(summing())

print("Максимальный элемент главной диагонали")

print(max_element())
