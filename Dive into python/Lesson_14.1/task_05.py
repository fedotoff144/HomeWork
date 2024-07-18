"""
Вам предоставлен код на Python из предыдущих задач, который содержит два класса: Rectangle и NegativeValueError.

Ваша задача - написать набор тестов для класса Rectangle, чтобы убедиться,
что он работает правильно и обрабатывает некорректные значения.

Тесты должны быть написаны с использованием модуля pytest.
*Тесты необходимо написать именно в этом порядке!

Тесты:
- test_width: Тестирование инициализации ширины. Создайте объект Rectangle с шириной 5 и убедитесь,
  что ширина установлена правильно.
- test_height: Тестирование инициализации ширины и высоты. Создайте объект Rectangle с шириной 3 и
  высотой 4 и убедитесь, что высота установлена правильно.
- test_perimeter: Тестирование вычисления периметра. Создайте объект Rectangle с шириной 5 и
  вычислите его периметр (должен быть равен 20).
- test_area: Тестирование вычисления площади. Создайте объект Rectangle с шириной 3 и высотой 4 и
  вычислите его площадь (должна быть равна 12).
- test_addition: Тестирование операции сложения двух прямоугольников. Создайте два объекта
  Rectangle с ширинами 5 и 3, и высотами 1 и 4 соответственно. Произведите операцию сложения и
  убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты.
- test_negative_width: Тестирование инициализации отрицательной ширины. Попробуйте создать объект
  Rectangle с отрицательной шириной (-5) и убедитесь, что это вызывает исключение NegativeValueError.
- test_negative_height: Тестирование инициализации отрицательной высоты. Попробуйте создать объект
  Rectangle с шириной 5 и отрицательной высотой (-4) и убедитесь, что это вызывает исключение NegativeValueError.
- test_set_width: Тестирование изменения ширины. Создайте объект Rectangle с шириной 5 и измените
  его ширину на 10. Убедитесь, что ширина изменена правильно.
- test_set_negative_width: Тестирование изменения отрицательной ширины. Создайте объект Rectangle с
  шириной 5 и попробуйте изменить его ширину на отрицательное значение (-10). Убедитесь,
  что это вызывает исключение NegativeValueError.
- test_set_height: Тестирование изменения высоты. Создайте объект Rectangle с шириной 3 и
  высотой 4 и измените его высоту на 6. Убедитесь, что высота изменена правильно.
- test_set_negative_height: Тестирование изменения отрицательной высоты. Создайте объект Rectangle
  с шириной 3 и высотой 4 и попробуйте изменить его высоту на отрицательное значение (-6).
  Убедитесь, что это вызывает исключение NegativeValueError.
- test_subtraction: Тестирование операции вычитания двух прямоугольников. Создайте два объекта
  Rectangle с ширинами 10 и 3, и высотами 1 и 4 соответственно. Произведите операцию вычитания и
  убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты.
- test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом.
  Создайте два объекта Rectangle с ширинами 3 и 10, и высотами 4 и 1 соответственно. Попробуйте
  выполнить операцию вычитания и убедитесь, что это вызывает исключение NegativeValueError.
- test_subtraction_same_perimeter: Тестирование операции вычитания с одинаковым периметром.
  Создайте два объекта Rectangle с ширинами 5 и 4, и высотами 1 и 3 соответственно. Произведите
  операцию вычитания и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты.

Запускать тесты не надо, автотест это сделает сам:

# Запускаем pytest.main() с нужными параметрами
    pytest.main(["--no-header", '-q', "--durations=0", new_filename])

На выходе после автоматической обрезки информации в тестах вы должны получить:
....F.......FF                                                           [100%]
"""
import pytest


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

# Введите ваше решение ниже
