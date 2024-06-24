"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.
"""
with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write("""
    import csv
import json
import random


def generate_csv_file(file_name, rows):
    with open(file_name, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(100, 1000) for _ in range(3)]
            csv_writer.writerow(row)


def save_to_json(func):
    def wrapper(file_name):
        data = []
        with open(file_name, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                data.append({"parameters": [a, b, c], "result": roots})

        with open('results.json', 'w') as f:
            json.dump(data, f, indent=4)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
    """)
