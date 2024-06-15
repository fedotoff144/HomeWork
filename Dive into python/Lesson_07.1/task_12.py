"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
Создайте файл __init__.py и запишите в него функцию rename_files
"""
with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write("""
    from pathlib import Path


def rename_files(desired_name, num_digits, source_ext, target_ext):
    path = Path.joinpath(Path.cwd(), 'test_folder')
    counter = 1
    for obj in path.glob(f"*.{source_ext}"):
        new_file_name = f'{desired_name}{counter:0{num_digits}}.{target_ext}'
        counter += 1
        obj.rename(path / new_file_name)
    """)
