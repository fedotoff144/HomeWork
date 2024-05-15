"""
Задание №2
📌 Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
📌 При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-
архивов
📌 list-архивы также являются свойствами экземпляра
"""


class Archive:
    _lines_archive = []
    _nums_archive = []
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._last is not None:
            Archive.add_record(Archive._last)
        cls._last = super().__new__(cls)
        return cls._last

    def __init__(self, num: int, line: str):
        self.num = num
        self.line = line

    def add_record(self):
        Archive._lines_archive.append(self.line)
        Archive._nums_archive.append(self.num)

    def lines_archive(self):
        return Archive._lines_archive

    def nums_archive(self):
        return Archive._nums_archive


arch1 = Archive(15, 'Yes')
print(f'{arch1.num=}\t{arch1.line=}')
print(f'Nums archive: {arch1.nums_archive()}\tL'
      f'ines archive: {arch1.lines_archive()}\n')

arch2 = Archive(10, 'No')
print(f'{arch2.num=}\t{arch2.line=}')
print(f'Nums archive: {arch2.nums_archive()}\t'
      f'Lines archive: {arch2.lines_archive()}\n')

arch3 = Archive(5, 'Maybe')
print(f'{arch3.num=}\t{arch3.line=}')
print(f'Nums archive: {arch3.nums_archive()}\t'
      f'Lines archive: {arch3.lines_archive()}\n')
