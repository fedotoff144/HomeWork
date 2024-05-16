"""
Задание №4
- Доработаем класс Архив из задачи 2.
- Добавьте методы представления экземпляра для программиста
и для пользователя.
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
        return (f'Экземпляр класса Archive с аргументами: '
                f'num - {self.num}\tstring - {self.string}')

    def __repr__(self):
        """Returns the official string representation of the class instance."""
        return f'Archive({self.num}, {self.string})'

    def add_record(self):
        """Adds the current num and string values to the archive."""
        Archive._strings_archive.append(self.string)
        Archive._nums_archive.append(self.num)

    def lines_archive(self):
        """Returns the archived strings."""
        return Archive._strings_archive

    def nums_archive(self):
        """Returns the archived numbers."""
        return Archive._nums_archive


arch1 = Archive(15, 'Yes')
print(arch1)
print(repr(arch1))

arch2 = Archive(10, 'No')
print(f'{arch2=}\n{arch2}')

arch3 = Archive(5, 'Maybe')
print(f'{arch3=}\n{arch3}')
