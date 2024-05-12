"""
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person:
    def __init__(self, firstname, lastname, age, phone, surname=None):
        self.firstname = firstname
        self.lastname = lastname
        self.surname = surname
        self.__age = age
        self.phone = phone

    def full_name(self):
        return f'Фамилия: {self.lastname}, Имя: {self.firstname} , Отчество: {self.surname}' \
            if self.surname else f'Фамилия: {self.lastname}, Имя: {self.firstname}'

    def birthday(self):
        self.__age += 1

    def full_info(self):
        return f'{self.firstname=}, {self.lastname=}, {self.surname=}, ' +\
            f'{self.__age=}, {self.phone=}'


pers1 = Person("Иван", "Иванов", 18, 8905353, "Иванович")
print(pers1.full_name())

pers1.birthday()
print(pers1._Person__age)

print(pers1.full_info())
