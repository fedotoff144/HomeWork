"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.

Пример использования.

На входе:
queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]

На выходе:
False
"""
queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


def show_table(queens: list[tuple]):
    table = [[0 for _ in range(8)] for _ in range(8)]
    for q in queens:
        table[q[1] - 1][q[0] - 1] = 1
    for _ in table:
        print(_)


def is_attacking(q1: tuple, q2: tuple) -> bool:
    x1, y1 = q1
    x2, y2 = q2

    if x1 == x2 or y1 == y2:
        return False

    while x1 <= 8 or y1 <= 8:
        x1 += 1
        y1 += 1
        if x1 == x2 and y1 == y2:
            return False

    x1, y1 = q1
    x2, y2 = q2
    while x1 <= 8 or y1 >= 1:
        x1 += 1
        y1 -= 1
        if x1 == x2 and y1 == y2:
            return False

    x1, y1 = q1
    x2, y2 = q2
    while x1 >= 1 or y1 >= 1:
        x1 -= 1
        y1 -= 1
        if x1 == x2 and y1 == y2:
            return False

    x1, y1 = q1
    x2, y2 = q2
    while x1 >= 1 or y1 <= 8:
        x1 -= 1
        y1 += 1
        if x1 == x2 and y1 == y2:
            return False

    return True


def check_queens(queens: list[tuple]) -> bool:
    if len(queens) <= 1:
        return True

    for i, q in enumerate(queens[:-1]):
        for q_next in queens[i + 1:]:
            if not is_attacking(q, q_next):
                return False


if __name__ == '__main__':
    queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
    show_table(queens)
    print(check_queens(queens))
