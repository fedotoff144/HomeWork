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


def csv_generation(range_a: int, range_b: int):
    """generates the specified number of lines of random values
    within the specified limits into a file.
    """
    num_rows = random.randint(100, 1000)
    with open('nums.csv', 'w', newline='', encoding='utf-8') as f:
        write_line = csv.writer(f, dialect='excel',
                                quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(num_rows):
            row = random.sample(range(range_a, range_b), 3)
            write_line.writerow(row)


def deco_find_roots(func: Callable):
    """A decorator that runs a function to find the roots
    of a quadratic equation with each triple of numbers from a csv file.
    """
    def wrapper():
        with open('nums.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                func(a, b, c)

    return wrapper


def deco_logger(func: Callable):
    """A decorator that saves the passed parameters
    and the results of the function to a json file.
    """
    def wrapper(*args):
        result = func(*args)
        record = {'parameters': f'a= {args[0]}, b= {args[1]}, c= {args[2]}',
                  'result': result}
        with open('results.json', 'a', encoding='utf-8') as f:
            json.dump(record, f, ensure_ascii=False)

    return wrapper


# first way to decorate a mathematical function
# @deco_find_roots
# @deco_logger
def math_function(a, b, c):
    """Calculate the roots of a square."""
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


csv_generation(-10, 10)
# second way to decorate a mathematical function
math_with_logger = deco_logger(math_function)
whole_deco_math = deco_find_roots(math_with_logger)
whole_deco_math()
