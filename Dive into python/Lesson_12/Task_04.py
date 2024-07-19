"""
Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:

    def __init__(self, a, b=None):
        self._a = a
        self._b = b if b else a

    @property
    def side_handler(self):
        return f'{self._a=}, {self._b=}'

    @side_handler.setter
    def side_handler(self, args):
        if isinstance(args, int):
            args = (args, args)
        a, b = map(int, args)
        if a <= 0 or b <= 0:
            raise ValueError('Values incorrect, try again')
        else:
            self._a = a
            self._b = b

    def square(self):
        return self._a * self._b

    def perimetr(self):
        return 2 * self._a + 2 * self._b


if __name__ == '__main__':
    rect_1 = Rectangle(4)
    rect_2 = Rectangle(2, 7)
    print(f'rect_1= {rect_1.side_handler}')
    rect_1.side_handler = 10, 9
    print(f'rect_1= {rect_1.side_handler}')
    print(f'rect_2= {rect_2.side_handler}')
    rect_2.side_handler = 3
    print(f'rect_2= {rect_2.side_handler}')
