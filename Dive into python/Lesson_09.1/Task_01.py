"""
Напишите следующие функции:
1. Нахождение корней квадратного уравнения
2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
3. Декоратор, запускающий функцию нахождения корней квадратного уравнения
   с каждой тройкой чисел из csv файла.
4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import csv
import json
import math
import random
from typing import Callable


def math_function(a, b, c):
    """Calculate the roots of a square"""
    try:
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1, x2 = (-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (
                    2 * a)
            return x1, x2
        elif d == 0:
            x = -b / (2 * a)
            return x
        else:
            return 'Корней нет'
    except ZeroDivisionError:
        return 'Деление на 0'


def csv_generation(num_rows: int, range_a: int, range_b: int):
    with open('nums.csv', 'w', newline='', encoding='utf-8') as f:
        write_line = csv.writer(f, dialect='excel',
                                quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(num_rows):
            row = random.sample(range(range_a, range_b), 3)
            write_line.writerow(row)


def deco_find_roots(func: Callable):
    def wrapper():
        all_data = []
        with open('nums.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                all_data.append({'parameters': {'a': a, 'b': b, 'c': c},
                                 'result': result})
        return all_data
    return wrapper


def deco_logger(func: Callable):
    def wrapper():
        result = func()
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        return result
    return wrapper


@deco_find_roots
@deco_logger
def run_math():
    return math_function()
