"""
1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
   и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
2. Для дочерних объектов указывайте родительскую директорию.
3. Для каждого объекта укажите файл это или директория.
4. Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
   с учётом всех вложенных файлов и директорий.


Пример:
test/users/names.txt
Результат в json для names.txt:
{
"name": names.txt
"parent": users,
"type": "file"
"size": 4096
}

3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.


Дополнительно:
Решить задания, которые не успели решить на семинаре(6, 7)
"""
import csv
import json
import pickle
from pathlib import Path

__all__ = []


def get_list_files(path: str):
    home_dir = Path(path)
    structure_list = []
    for obj in home_dir.rglob('*'):
        print(f'{obj.parts[-2]}\t{"File" if obj.is_file() else "Directory"}\t{obj=}')


if __name__ == '__main__':
    path_dir = 'D:\GeekBrains\HomeWork\Dive into python\Lesson_08.1'
    get_list_files(path_dir)
