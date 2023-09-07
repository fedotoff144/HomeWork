import os
import csv
import json
import pickle

__all__ = ['scan_files', 'create_json_file', 'create_csv_file', 'create_binary_file']


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
        csv_writer = csv.DictWriter(f, fieldnames=["name", "parent", "type", "size"], dialect='excel', quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
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
