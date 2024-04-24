"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

path = 'C:\Program Files (x86)\Samsung\Samsung M2070 Series\Setup\setup.exe'


def file_path_handling(text):
    *path_file, file = text.split('\\')
    file_name, file_extension = file.split('.')
    return '\\'.join(path_file), file_name, file_extension


print(file_path_handling(path))
