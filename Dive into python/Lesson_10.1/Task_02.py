"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def area_rectangle(self):
        return self.length * self.width


rect1 = Rectangle(5, 10)
print(rect1.perimeter())
print(rect1.area_rectangle())
