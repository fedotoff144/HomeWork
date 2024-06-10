"""
Напишите функцию get_file_info, которая принимает на вход строку -
абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Пример использования.

На входе:
file_path = "C:/Users/User/Documents/example.txt"

На выходе:
('C:/Users/User/Documents/', 'example', '.txt')
"""
import pathlib

file_path = '/home/user/docs/my.file.with.dots.txt'


def get_file_info(absolute_path: str) -> tuple:
    path = pathlib.Path(absolute_path)
    file_location = str(path.parent).replace('\\', '/') + '/' \
        if len(str(path.parent)) > 1 else ''
    file_name = path.name.rpartition('.')[0]
    file_extension = path.suffix
    return file_location, file_name, file_extension


print(get_file_info(file_path))
