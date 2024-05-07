"""
Напишите следующие функции:
1. Нахождение корней квадратного уравнения
2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
3. Декоратор, запускающий функцию нахождения корней квадратного уравнения
   с каждой тройкой чисел из csv файла.
4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import csv
import math
import random
from typing import Callable


def csv_generation(num_rows: int, range_a: int, range_b: int):
    with open('nums.csv', 'w', newline='', encoding='utf-8') as f:
        write_line = csv.writer(f, dialect='excel',
                                quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(num_rows):
            row = random.choices(range(range_a, range_b), k=3)
            write_line.writerow(row)


def deco_find_roots(func: Callable):
    with open('nums.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b, c = map(int, row)
            result = func(a, b, c)
            print(result)


@deco_find_roots
def math_function(a: int, b: int, c: int):
    try:
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1, x2 = (-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)
            return x1, x2
        elif d == 0:
            x = -b / (2 * a)
            return x
        else:
            return 'Корней нет'
    except ZeroDivisionError:
        return 'Деление на 0'


math_function()
