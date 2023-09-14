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
CSV_FILENAME = 'numbers.csv'


def generate_csv_file():
    with open(CSV_FILENAME, 'w', newline='') as f:
        for i in range(FILE_SIZE):
            temp_int = random.randint(100, 999)
            f.write(f'{temp_int}\n')


def read_csv_file():
    with open(CSV_FILENAME, 'r', newline='', encoding='utf-8') as f:
        list_nums = []
        reader = csv.reader(f)
        for line in reader:
            list_nums.append(line)
    return list_nums


def deco_func_json(func: Callable):
    def wrapper(*args, **kwargs):
        with open('result.json', 'a', encoding='utf-8') as f:
            my_list = []
            for line in args:
                function_result = func(*line)
                my_list.append({'arguments': line, 'result': function_result})
            json.dump(my_list, f, ensure_ascii=False)
            return my_list

    return wrapper


def deco_func_equation(func: Callable):
    def wrapper(*args, **kwargs):
        for trinity in args:
            a, b, c = map(int, str(trinity))
            result = func(a, b, c)
        return result

    return wrapper


@deco_func_json
@deco_func_equation
def find_equation_roots(a, b, c):
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


generate_csv_file()
data = read_csv_file()
find_equation_roots(*data)
