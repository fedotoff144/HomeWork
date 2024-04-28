import random

__all__ = ['generation_random_comb', 'perpendicular_intersection_check',
           'diagonal_intersection_check', 'chessboard_drawing',
           'chessboard_print']


def generation_random_comb(len_comb: int) -> list[tuple]:
    """Random combination generator"""
    set_coordinates = [i for i in range(len_comb)] * 2
    random.shuffle(set_coordinates)
    combination = []
    for i in range(len_comb):
        x = set_coordinates[i]
        y = set_coordinates[len_comb + i]
        combination.append((x, y))
    return combination


def perpendicular_intersection_check(combination: list[tuple],
                                     size_chessboard: int) -> bool:
    """
    If the number of elements of the row set and the column set
    is equal to the number of squares of the chessboard on one side,
    then the queens are not located in the same rows or columns
    """
    row = {i[0] for i in combination}
    column = {i[1] for i in combination}
    return len(row) == size_chessboard and len(column) == size_chessboard


def diagonal_intersection_check(combinations: list[tuple],
                                size_chessboard: int) -> bool:
    """Checks whether the diagonals of each queen
    intersect the coordinates of other queens
    """
    for item in combinations:
        all_directions = []
        reduced_list = combinations.copy()
        reduced_list.remove(item)
        x, y = item[0], item[1]

        while True:
            if x == size_chessboard - 1 or y == size_chessboard - 1:
                x, y = item[0], item[1]
                break
            x += 1
            y += 1
            temp_tuple = x, y
            all_directions.append(temp_tuple)

        while True:
            if x == 0 or y == 0:
                x, y = item[0], item[1]
                break
            x -= 1
            y -= 1
            temp_tuple = x, y
            all_directions.append(temp_tuple)

        while True:
            if x == size_chessboard - 1 or y == 0:
                x, y = item[0], item[1]
                break
            x += 1
            y -= 1
            temp_tuple = x, y
            all_directions.append(temp_tuple)

        while True:
            if x == 0 or y == size_chessboard - 1:
                break
            x -= 1
            y += 1
            temp_tuple = x, y
            all_directions.append(temp_tuple)

        for i in all_directions:
            if i in reduced_list:
                return False

    return True


def chessboard_drawing(combination: list[tuple],
                       size_chessboard: int) -> list[list]:
    """Creates a console representation of the position of the pieces
    on the chessboard according to the passed combination
    """
    chessboard = [[0] * size_chessboard for _ in range(size_chessboard)]

    for i in combination:
        index_0 = i[1]
        index_1 = i[0]
        chessboard[index_0][index_1] = 1
    return chessboard


def chessboard_print(chessboard: list[list]):
    """Prints a console view of the pieces on a chessboard"""
    for _ in chessboard:
        print(_)


if __name__ == '__main__':
    chessboard_size: int = 8
    safe_combinations = []

    while len(safe_combinations) != 3:
        comb = generation_random_comb(chessboard_size)
        if (perpendicular_intersection_check(comb, chessboard_size) and
                diagonal_intersection_check(comb, chessboard_size)):
            safe_combinations.append(comb)

    for i, j in enumerate(safe_combinations, start=1):
        print(f'РАССТАНОВКА {i}')
        chessboard_print(chessboard_drawing(j, chessboard_size))
