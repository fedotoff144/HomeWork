"""
Задание №2
- Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
- При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-
архивов
- list-архивы также являются свойствами экземпляра
"""


class Archive:
    """The Archive class is designed for storing and archiving numbers and strings."""
    _strings_archive = []
    _nums_archive = []
    _last = None

    def __new__(cls, *args, **kwargs):
        """
        Method is used to create a new instance of the class.
        It also preserves the last created instance of the class.
        """
        if cls._last is not None:
            Archive.add_record(Archive._last)
        cls._last = super().__new__(cls)
        return cls._last

    def __init__(self, num: int, string: str):
        """Initializes an instance of the class with the provided number and string."""
        self.num = num
        self.string = string

    def __str__(self):
        """Returns a string representation of the class instance."""
        return f'Instance Archive class. num: {self.num}, string: {self.string}'

    def __repr__(self):
        """Returns the official string representation of the class instance."""
        return f'Archive({self.num}, {self.string})'

    def add_record(self):
        """Adds the current num and string values to the archive."""
        Archive._strings_archive.append(self.string)
        Archive._nums_archive.append(self.num)

    def strings_archive(self):
        """Returns the archived strings."""
        return Archive._strings_archive

    def nums_archive(self):
        """Returns the archived numbers."""
        return Archive._nums_archive


arch1 = Archive(15, 'Yes')
print(f'{arch1.num=}\t{arch1.string=}')
print(f'Nums archive: {arch1.nums_archive()}\tL'
      f'ines archive: {arch1.strings_archive()}\n')

arch2 = Archive(10, 'No')
print(f'{arch2.num=}\t{arch2.string=}')
print(f'Nums archive: {arch2.nums_archive()}\t'
      f'Lines archive: {arch2.strings_archive()}\n')

arch3 = Archive(5, 'Maybe')
print(f'{arch3.num=}\t{arch3.string=}')
print(f'Nums archive: {arch3.nums_archive()}\t'
      f'Lines archive: {arch3.strings_archive()}\n')
