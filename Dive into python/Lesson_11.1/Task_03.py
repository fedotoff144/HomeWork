"""
Задание №3
- Добавьте к задачам 1 и 2 строки документации для классов.
"""
import time


class MyString(str):
    """A class that complements the capabilities of the str class."""

    def __new__(cls, value: str, author: str = 'unknown'):
        """Determines what should be returned class as itself - class."""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.ctime(time.time())
        return instance


class Archive:
    """The Archive class stores a pair of properties: number and string.
    When creating a new instance of a class, the old data from previously
    created instances are saved in a pair of lists - archives"""
    _strings_archive = []
    _nums_archive = []
    _last = None

    def __new__(cls, *args, **kwargs):
        """Returns a class as itself, recording information
        about previously created classes in lists."""
        if cls._last is not None:
            Archive.add_record(Archive._last)
        cls._last = super().__new__(cls)
        return cls._last

    def __init__(self, num: int, string: str):
        """Initialization method."""
        self.num = num
        self.string = string

    def add_record(self):
        """The method adds records about the old class
        when creating a new one."""
        Archive._strings_archive.append(self.string)
        Archive._nums_archive.append(self.num)

    def lines_archive(self):
        """Returns a list of string properties
        of previously created instances of the class."""
        return Archive._strings_archive

    def nums_archive(self):
        """Returns a list of integer properties
        of previously created instances of the class."""
        return Archive._nums_archive


print(help(MyString))
print(MyString.__new__.__doc__)

print(help(Archive))
print(Archive.add_record.__doc__)
