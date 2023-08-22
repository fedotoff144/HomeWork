"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def split_path(path: str) -> tuple:
    # сплитуем путь по "\"
    path_split = path.split('\\')
    file = path_split[-1].split('.')

    # удаляем последний элемент списка - название файла и его расширение
    path_split.pop()

    # собираем имя пути обратно через "\"
    file_path = '\\'.join(path_split)

    tuple_link = (file_path, file[0], file[1])
    return tuple_link


absolute_path = 'C:\Windows\System32\Ru-RU\Licenses\OEM\Professional\license.rtf'
path_elements = split_path(absolute_path)
print(f'путь к файлу={path_elements[0]}\n'
      f'имя файла={path_elements[1]}\n'
      f'расширение файла={path_elements[2]}')
