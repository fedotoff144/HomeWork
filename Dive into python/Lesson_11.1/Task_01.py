"""
Задание №1
- Создайте класс Моя Строка, где:
- будут доступны все возможности str
- дополнительно хранятся имя автора строки и время создания
(time.time)
"""
import time


class MyString(str):

    def __new__(cls, value: str, author: str = 'unknown'):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.ctime(time.time())
        return instance


my_str = MyString('Some value of string', 'Pushkin A.S.')

print(f'{my_str=}\t{my_str.author=}\t{my_str.time=}\t{type(my_str)}')
