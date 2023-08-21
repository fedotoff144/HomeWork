"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os


def split_file_path(absolute_path):
    directory, file_name = os.path.split(absolute_path)
    file_name, file_extension = os.path.splitext(file_name)
    result = (directory, file_name, file_extension)
    return result


absolute_path = 'C:\Windows\System32\Ru-RU\Licenses\OEM\Professional\license.rtf'

print(split_file_path(absolute_path))
