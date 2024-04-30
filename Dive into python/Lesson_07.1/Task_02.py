"""
Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов.
  При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла.
  Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени.
  Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
  К ним прибавляется желаемое конечное имя, если оно передано.
  Далее счётчик файлов и расширение.

Пример:
rename(wanted_name = "video", count_nums=3, extension_old=".csv", extension_new=".txt", diapazon=[3, 6])
foto_2002.txt -> o_20video001.csv

"""
from pathlib import Path


def rename_files(wanted_name: str, count_nums: int, extension_old: str,
                 extension_new: str, diapazon: list):
    # get home directory
    pwd = Path.cwd()
    # set counter changed files
    count_files = 1

    slice_extension = len(extension_old)

    for obj in pwd.iterdir():
        if str(obj)[-slice_extension:] == extension_old:
            # set counter to needed format
            count_str = '0' * (count_nums - len(str(count_files))) + \
                        str(count_files)
            # get slice of old file name
            old_file_name = obj.name[diapazon[0]:diapazon[1]]
            # assemble the name and rename the object
            new_file_name = old_file_name + wanted_name + count_str + \
                            extension_new
            obj.rename(new_file_name)
            count_files += 1


rename_files('_note_', 4, '.txt',
             '.txt', [0, 4])
