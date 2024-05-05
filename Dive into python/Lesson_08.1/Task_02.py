"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def my_func(input_file, output_file):
    with(
        open(input_file, 'r', encoding='utf-8') as f_txt,
        open(output_file, 'w', encoding='utf-8') as f_json
    ):
        data = f_txt.readlines()
        all_data = {}
        for i in data:
            line = i.split()
            key = line[0].capitalize()
            value = int(line[1]) if line[1].isdigit() else float(line[1])
            all_data[key] = value
        json.dump(all_data, f_json)


my_func('pairs_num_name.txt', 'pairs_num_name.json')
