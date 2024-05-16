"""
Задание №5
- Дорабатываем класс прямоугольник из прошлого семинара.
- Добавьте возможность сложения и вычитания.
- При этом должен создаваться новый экземпляр
прямоугольника.
- Складываем и вычитаем периметры, а не длину и ширину.
- При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def perimeter(self):
        return (self.length + self.width) * 2

    def area_rectangle(self):
        return self.length * self.width

    # def __add__(self, other):
    #     length = self.length + other.length
    #     width = self.width + other.width
    #     return Rectangle(length, width)

    def __add__(self, other):
        return self.perimeter() + other.perimeter()

    # def __sub__(self, other):
    #     length = self.length - other.length
    #     width = self.width - other.width
    #     if length < 0 or width < 0:
    #         return 'Minus is not allowed'
    #     return Rectangle(length, width)

    def __sub__(self, other):
        result = self.perimeter() - other.perimeter()
        if result < 0:
            return 'Minus is not allowed'
        return result


rect1 = Rectangle(5, 10)
rect2 = Rectangle(5, 10)
print(rect1 + rect2)
print(rect1 - rect2)
