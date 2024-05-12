"""
Задача 1.
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.

"""
from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def circumference(self):
        return self.r * 2 * pi

    def area_circle(self):
        return self.r ** 2 * pi


c1 = Circle(110)
print(c1.circumference())
print(c1.area_circle())
