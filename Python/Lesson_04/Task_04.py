# Task 4

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random


def write_file(f):
    with open('file_task_04.txt', 'w') as data:
        data.write(f)


def create_polynom(k):
    str = ''
    while (k >= 0):
        if (k == 0):
            str += f'{random.randint(1, 101)} = 0'
            break
        str += f'{random.randint(1, 101)}x**{k} + '
        k -= 1
    return str


k = int(input("Введите натуральную степень k: "))
write_file(create_polynom(k))
