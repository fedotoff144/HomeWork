"""
Задание №6
- Доработайте прошлую задачу.
- Добавьте сравнение прямоугольников по площади
- Должны работать все шесть операций сравнения
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def __str__(self):
        return f'length: {self.length}\twidth: {self.width}'

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

    def __eq__(self, other):
        return self.area_rectangle() == other.area_rectangle()

    def __ne__(self, other):
        return self.area_rectangle() != other.area_rectangle()

    def __gt__(self, other):
        return self.area_rectangle() > other.area_rectangle()

    def __ge__(self, other):
        return self.area_rectangle() >= other.area_rectangle()

    def __lt__(self, other):
        return self.area_rectangle() < other.area_rectangle()

    def __le__(self, other):
        return self.area_rectangle() <= other.area_rectangle()


rect1 = Rectangle(10, 10)
rect2 = Rectangle(15, 10)
print(rect1, '\t', rect2)
print(f'+ {rect1 + rect2}\n- {rect1 - rect2}\n== {rect1 == rect2}\n'
      f'!= {rect1 != rect2}\n>= {rect1 >= rect2}\n<= {rect1 <= rect2}\n'
      f'> {rect1 > rect2}\n< {rect1 < rect2}')
