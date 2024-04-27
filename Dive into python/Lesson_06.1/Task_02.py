"""
Дополнительная задача:

    1. Добавьте в пакет, созданный на семинаре шахматный модуль.
    Внутри него напишите код, решающий задачу о 8 ферзях. Известно,
    что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
    Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
    бьющих друг друга. Программа получает на вход восемь пар чисел,
    каждое число от 1 до 8 - координаты 8 ферзей.
    Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

    2. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
    для случайной расстановки ферзей в задаче выше.
    Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

Пример, когда задача решена верно:
_table = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]
_SAFE_COMB_EXAMPLE = [(0, 0), (6, 1), (4, 2), (7, 3),
(1, 4), (3, 5), (5, 6), (2, 7)]
"""
from module_package import chess_module as cm

safe_combinations = []
chessboard_size: int = 8
len_safe_comb = 3

while len(safe_combinations) != len_safe_comb:
    comb = cm.generation_random_comb(chessboard_size)
    if (cm.perpendicular_intersection_check(comb, chessboard_size) and
            cm.diagonal_intersection_check(comb, chessboard_size)):
        safe_combinations.append(comb)

for i, j in enumerate(safe_combinations, start=1):
    print(f'\tРАССТАНОВКА {i}')
    cm.chessboard_print(cm.chessboard_drawing(j, chessboard_size))
