"""
Задание №4
- Доработаем класс Архив из задачи 2.
- Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    _strings_archive = []
    _nums_archive = []
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._last is not None:
            Archive.add_record(Archive._last)
        cls._last = super().__new__(cls)
        return cls._last

    def __init__(self, num: int, string: str):
        self.num = num
        self.string = string

    def __str__(self):
        return (f'Экземпляр класса Archive с аргументами: '
                f'num - {self.num}\tstring - {self.string}')

    def __repr__(self):
        return f'Archive({self.num}, {self.string})'

    def add_record(self):
        Archive._strings_archive.append(self.string)
        Archive._nums_archive.append(self.num)

    def lines_archive(self):
        return Archive._strings_archive

    def nums_archive(self):
        return Archive._nums_archive


arch1 = Archive(15, 'Yes')
print(arch1)
print(repr(arch1))

arch2 = Archive(10, 'No')
print(f'{arch2=}\n{arch2}')

arch3 = Archive(5, 'Maybe')
print(f'{arch3=}\n{arch3}')
