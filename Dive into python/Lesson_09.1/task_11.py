"""
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайных
числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл.
Функция принимает два аргумента:
file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида
ax^2 + bx + c = 0.
Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры
a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет
сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

Пример

На входе:
generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)

На выходе:
True
True
Формат JSON файла определён следующим образом:

[
    {"parameters": [a, b, c], "result": result},
    {"parameters": [a, b, c], "result": result},
    ...
]
"""
import csv
import json
from random import randint
from typing import Callable


def save_to_json(func: Callable):
    def wrapper(*args, **kwargs):
        with(
            open('results.json', 'w', encoding='utf-8') as file_4_write,
            open(args[0], 'r', newline='', encoding='utf-8') as file_4_read
        ):
            lst_4_write_json = []
            for i in file_4_read:
                i = i.replace('\r\n', '')
                a, b, c = map(int, i.split(','))
                result = func(a, b, c)
                lst_4_write_json.append({"parameters": [a, b, c], "result": result})
            json.dump(lst_4_write_json, file_4_write)

        return lst_4_write_json

    return wrapper


def generate_csv_file(file_name: str, rows: int):
    if rows < 100:
        rows = 100
    elif rows > 1000:
        rows = 1000
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        f_writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(rows):
            row = randint(-10, 10), randint(-10, 10), randint(-10, 10)
            f_writer.writerow(row)


@save_to_json
def find_roots(a: int, b: int, c: int) -> None | tuple | int:
    d = b ** 2 - 4 * a * c
    if d > 0:
        try:
            x_1 = (b * (-1) - d ** 0.5) / (2 * a)
            x_2 = (b * (-1) + d ** 0.5) / (2 * a)
            return x_1, x_2
        except ZeroDivisionError:
            return None
    elif d == 0:
        x = b * (-1) / 2 * a
        return x
    else:
        return None


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 200)
    find_roots('input_data.csv')
