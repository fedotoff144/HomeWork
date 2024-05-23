"""
Задание №1
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

lst = [1, 20.5, 'Hello world', True, [0, 1, 2], (3, 4), {'one': 1, 'two': 2},
       {1, 2, 3}]

for i, _ in enumerate(lst, start=1):
    print(f'{i}\t{_}\t'
          f'{id(_)}\t'
          f'{_.__sizeof__()}\t'
          f'{hash(_) if not isinstance(_, (list, dict, set)) else "unhashable type"}\t'
          f'{True if isinstance(_, int) else None}\t'
          f'{True if isinstance(_, str) else None}')
