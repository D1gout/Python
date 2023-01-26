import re
i = str(input("Введите время в формате\n**:**\n"))

s = re.fullmatch(r'[0-2][0-9]:[0-5][0-9]', i)
if s:
    print(f'Ваше время {i}')
