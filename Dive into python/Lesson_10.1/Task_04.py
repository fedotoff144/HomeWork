"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
# from Task_03 import Person

class Employee():
    def __init__(self, empl_id):

        self.id =
        # self.access_level =

    def show_data(self):
        return self.id

empl1 = Employee(123456)
print(empl1.show_data())