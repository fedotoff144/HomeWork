"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

"""
from pathlib import Path


def sorting_files(path):
    home_dir = Path(path)

    # create necessary folders for sorting
    if not Path(home_dir / 'pictures').exists():
        Path.mkdir(home_dir / 'pictures')
    if not Path(home_dir / 'video').exists():
        Path.mkdir(home_dir / 'video')
    if not Path(home_dir / 'text').exists():
        Path.mkdir(home_dir / 'text')
    if not Path(home_dir / 'music').exists():
        Path.mkdir(home_dir / 'music')

    for obj in home_dir.rglob('*'):
        if obj.is_file():
            if obj.name.endswith('.jpg') or obj.name.endswith('.png'):
                obj.replace(home_dir / 'pictures' / obj.name)
            if obj.name.endswith('.mp4') or obj.name.endswith('.avi'):
                obj.replace(home_dir / 'video' / obj.name)
            if obj.name.endswith('.txt') or obj.name.endswith('.csv') \
                    or obj.name.endswith('.doc') or obj.name.endswith('.docx') \
                    or obj.name.endswith('.pdf'):
                obj.replace(home_dir / 'text' / obj.name)
            if obj.name.endswith('.mp3') or obj.name.endswith('.aac'):
                obj.replace(home_dir / 'music' / obj.name)


sorting_files('H:\SamsungPhone')
