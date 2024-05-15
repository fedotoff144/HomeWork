"""
Задание №5
- Дорабатываем класс прямоугольник из прошлого семинара.
- Добавьте возможность сложения и вычитания.
- При этом должен создаваться новый экземпляр
прямоугольника.
- Складываем и вычитаем периметры, а не длинну и ширину.
- При вычитании не допускайте отрицательных значений.
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
