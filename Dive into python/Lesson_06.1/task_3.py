"""
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей
на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами,
ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

Пример использования На входе:
print(generate_boards())

На выходе:
[
    [(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
    [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
    [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
    [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]
]
"""
import random
import task_2

board_list = []


def generate_boards() -> list[tuple]:
    """Returns a randomly generated list of queens coordinates."""
    rows = (1, 2, 3, 4, 5, 6, 7, 8)
    columns = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(columns)
    return [(rows[i], columns[i]) for i in range(8)]


if __name__ == '__main__':
    board_list = []
    while len(board_list) <= 3:
        combination = generate_boards()
        if task_2.check_queens(combination):
            board_list.append(combination)

    for _ in board_list:
        task_2.show_table(_)
        print()
