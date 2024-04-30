"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

"""
from pathlib import Path


def sorting_files(home_dir: str):
    for obj in home_dir.iterdir():
        if obj.is_file():
            if obj.name.__contains__('.jpg') or obj.name.__contains__('.png'):
                obj.replace(home_dir / 'pictures' / obj.name)
            if obj.name.__contains__('.mp4') or obj.name.__contains__('.avi'):
                obj.replace(home_dir / 'video' / obj.name)
            if obj.name.__contains__('.txt') or obj.name.__contains__('.csv'):
                obj.replace(home_dir / 'text' / obj.name)


sorting_files(Path.cwd())
