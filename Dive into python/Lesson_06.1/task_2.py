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
__all__ = ['show_table', 'check_queens']

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


def show_table(combinations: list[tuple]) -> None:
    """Displays the arrangement of queens on the chessboard."""
    chessboard = [[0 for _ in range(8)] for _ in range(8)]
    for comb in combinations:
        chessboard[comb[0] - 1][comb[1] - 1] = 1
    for _ in chessboard:
        print(_)


def is_attacking(q1: tuple, q2: tuple) -> bool:
    """The function checks whether the queens beat each other."""
    row1, column1 = q1
    row2, column2 = q2

    while row1 <= 8 or column1 <= 8:
        row1 += 1
        column1 += 1
        if row1 == row2 and column1 == column2:
            return False

    row1, column1 = q1
    row2, column2 = q2
    while row1 <= 8 or column1 >= 1:
        row1 += 1
        column1 -= 1
        if row1 == row2 and column1 == column2:
            return False

    row1, column1 = q1
    row2, column2 = q2
    while row1 >= 1 or column1 >= 1:
        row1 -= 1
        column1 -= 1
        if row1 == row2 and column1 == column2:
            return False

    row1, column1 = q1
    row2, column2 = q2
    while row1 >= 1 or column1 <= 8:
        row1 -= 1
        column1 += 1
        if row1 == row2 and column1 == column2:
            return False

    return True


def check_queens(queens: list[tuple]) -> bool:
    """Checks all possible pairs of queens."""
    if len(queens) <= 1:
        return True

    set_rows = {i[0] for i in queens}
    set_columns = {i[1] for i in queens}
    if len(set_rows) != 8 or len(set_columns) != 8:
        return False

    for i, q in enumerate(queens[:-1]):
        for q_next in queens[i + 1:]:
            if not is_attacking(q, q_next):
                return False
    return True


if __name__ == '__main__':
    queens = [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]
    show_table(queens)
    print(check_queens(queens))
