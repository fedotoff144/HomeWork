"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
import re
import random


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
        return f'{self.firstname=}, {self.lastname=}, {self.surname=}, ' + \
            f'{self.__age=}, {self.phone=}'


class Employee(Person):
    def __init__(self, empl_id, *args, **kwargs):
        pattern = r'^\d{6}$'
        if not re.match(pattern, str(empl_id)):
            self.empl_id = random.randint(100000, 999999)
        else:
            self.empl_id = empl_id
        id_sum = sum(int(i) for i in str(self.empl_id))
        self.access_level = id_sum % 7
        super().__init__(*args, **kwargs)

    def show_data(self):
        return self.full_info() + f', {self.empl_id=}, {self.access_level=}'


empl1 = Employee(987654, "Петр", "Петров", 20, 7960725, "Петрович")
print(empl1.show_data())
