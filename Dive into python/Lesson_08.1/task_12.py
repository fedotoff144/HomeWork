"""
Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory.
"""
with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write("""
import os
import json
import csv
import pickle


def get_dir_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            fp = os.path.join(root, file)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            path = os.path.join(root, name)
            if os.path.isfile(path):
                size = os.path.getsize(path)
                results.append({'Path': path, 'Type': 'File', 'Size': size})
            else:
                size = get_dir_size(path)
                results.append(
                    {'Path': path, 'Type': 'Directory', 'Size': size})
    return results


def save_results_to_json(results, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


def save_results_to_csv(results, filename):
    fieldnames = ['Path', 'Type', 'Size']
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)


def save_results_to_pickle(results, filename):
    with open(filename, 'wb') as file:
        pickle.dump(results, file)
    """)
