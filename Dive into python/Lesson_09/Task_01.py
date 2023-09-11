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
import random
from typing import Callable

FILE_SIZE = 100


def generate_csv_file():
    with open('numbers.csv', 'w', newline='') as f:
        for i in range(FILE_SIZE):
            temp_int = random.randint(100, 999)
            f.write(f'{temp_int}\n')


def write_json_file(data: dict):
    with open('json_result.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def deco_func_equation(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


@deco_func_equation
def find_equation_roots(a: int, b: int, c: int):
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        x1 = (-b + (d ** 0.5)) / (2 * a)
        x2 = (-b - (d ** 0.5)) / (2 * a)
        x = [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
    else:
        x = 'Корней нет'
    return x







