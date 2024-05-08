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
from modules import files_handling as fh

data = fh.get_list_files('D:\GeekBrains\HomeWork\Dive into python\Lesson_08.1')

fh.create_json_file(data)
fh.create_csv_file(data)
fh.create_binary_file(data)