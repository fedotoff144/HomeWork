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
rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
foto_2002.txt -> o_20video001.csv
"""
import os
from pathlib import Path


COUNT: int = 0
name = 'video'
count_nums = 3
extension_old = '.txt'
extension_new = '.csv'
diappazon = [3, 6]

def rename(wanted_name: str, count_nums: int, extension_old: str, extension_new: str, diapazon: list):
    files_list = os.listdir(os.getcwd())
    for file in files_list:
        if extension_old in file:
            temp = file.split('.')
            temp[0] = wanted_name + extension_new
    return None


files_list = os.listdir(os.getcwd())
for file in files_list:
    if extension_old in file:
        COUNT += 1
        file = f'{name}{COUNT}{extension_new}'



