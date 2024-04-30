"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.

"""
import random
from pathlib import Path


def filling_out_file(file_name:str, count_line:int):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(count_line):
            f.write(f'{random.randint(-1000, 1001)} | {random.uniform(-1000, 1001)}\n')


filling_out_file('fill_out.txt', 10)
