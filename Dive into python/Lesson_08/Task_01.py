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
import os
import csv
import json
import pickle

path = os.getcwd()


def scan_files(path: str) -> list:
    # сканируем все файлы по заданному пути
    scan_list = list(os.walk(path))

    # создаем пустой результирующий список который будет наполнен и возвращен функцией
    res_list = []

    for dir in scan_list:
        # поочередно получаем папки с файлами из отсканированого списка
        temp_list_files = os.listdir(dir[0])

        # обходим папку и собираем информацию о каждом файле в ней
        for file in temp_list_files:

            # создаем временный словарь и заполняем его иниформацией о файле
            temp_dict = {"name": file, "parent": dir[0].split('\\')[-1]}

            # собираем полный путь к файлу для проверки принадлежности к файлу или к папке
            full_path_file = os.path.join(dir[0], file)

            if os.path.isdir(full_path_file):
                temp_dict["type"] = "dir"
            elif os.path.isfile(full_path_file):
                temp_dict["type"] = "file"
            else:
                temp_dict["type"] = "unknown"

            temp_dict["size"] = os.path.getsize(full_path_file)

            # добавляем временный словарь с информацией о файле в результируюший список
            res_list.append(temp_dict)

    return res_list


def create_json_file(data: list):
    with(
        open('json_dump_file.json', 'w', encoding='utf-8') as f1,
        open('json_dumps_file.json', 'w', encoding='utf-8') as f2
    ):
        json.dump(data, f1)

        # data преобразуем сначала в строковое значение
        temp_str = json.dumps(data, ensure_ascii=False, indent=2, separators=('#', '| '), sort_keys=True)
        # записываем преобразованные данные в файл
        json.dump(temp_str, f2)


def create_csv_file(data: list):
    with open('csv_file.csv', 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=["name", "parent", "type", "size"], dialect='excel', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # записываем названия столбцов
        csv_writer.writeheader()
        # записываем данные столбцов
        csv_writer.writerows(data)


def create_binary_file(data: list):
    with(
        open('pickle_dump_file', 'wb') as f1,
        open('pickle_dumps_file', 'wb') as f2
    ):
        pickle.dump(data, f1)

        # data преобразуем сначала в строковое значение
        temp_str = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        # записываем преобразованные данные в файл
        pickle.dump(temp_str, f2)


data = scan_files(path)
create_json_file(data)
create_csv_file(data)
create_binary_file(data)
