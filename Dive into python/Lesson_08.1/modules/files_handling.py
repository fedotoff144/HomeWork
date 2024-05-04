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


def get_list_files(path: str) -> list[dict]:
    home_dir = Path(path)
    structure_list = []
    for obj in home_dir.rglob('*'):

        # it is not necessary
        if '.venv' in obj.parts:
            continue

        size_of_obj = obj.stat().st_size
        if obj.is_dir():
            for i in obj.rglob('*'):
                size_of_obj += i.stat().st_size

        temp_dict = {
            'name': obj.name,
            'parent': obj.parts[-2],
            'type': 'file' if obj.is_file() else 'directory',
            'size': size_of_obj
        }
        structure_list.append(temp_dict)
    return structure_list


def write_json_file(data: list):
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def read_json_file(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def create_csv_file(data: list):
    with open('result.csv', 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['name', 'parent', 'type', \
                                                   'size'], dialect='excel',
                                    quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def read_csv_file(file_name: str) -> list:
    with open(file_name, 'r', newline='', encoding='utf-8') as f:
        f_read = csv.DictReader(f,
                                fieldnames=['name', 'parent', 'type', 'size'],
                                dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        all_data = [line for i, line in enumerate(f_read) if i != 0]
    return all_data


def create_binary_file(data: list):
    with open('result.pickle', 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    path_dir = 'D:\GeekBrains\HomeWork\Dive into python\Lesson_08.1'
    list_of_structure = get_list_files(path_dir)

    # write_json_file(data)
    # output_json = read_json_file('result.json')
    # print(output_json)

    # create_csv_file(data)
    # output_csv = read_csv_file('result.csv')
    # print(output_csv)

    print(list_of_structure)
    create_binary_file(list_of_structure)
