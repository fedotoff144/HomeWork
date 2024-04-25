from random import randint

__all__ = []


def generation_comb(quantity: int) -> list[tuple]:
    """Random combination generator"""
    combination = [(randint(0, quantity), randint(0, quantity)) for _ in
                   range(quantity)]
    return combination


def chessboard_drawing(combination: list[tuple]) -> list[list]:
    """Creates a console representation of the position of the pieces
    on the chessboard according to the passed combination
    """
    chessboard = [[0] * len(combination) for _ in range(len(combination))]

    for i in combination:
        index_0 = i[0]
        index_1 = i[1]
        chessboard[index_0][index_1] = 1
    return chessboard


def chessboard_print(chessboard: list[list]):
    """Prints a console view of the pieces on a chessboard"""
    for _ in chessboard:
        print(_)


def perpendicular_intersection_check(combination: list[tuple],
                                     len_chess_board: int) -> bool:
    """
    If the number of elements of the row set and the column set
    is equal to the number of squares of the chessboard on one side,
    then the queens are not located in the same rows or columns
    """
    row = {i[0] for i in combination}
    column = {i[1] for i in combination}
    return len(row) == len_chess_board and len(column) == len_chess_board


if __name__ == '__main__':
    comb = [(0, 0), (6, 1), (4, 2), (7, 3), (1, 4), (3, 5), (5, 6), (2, 7)]
    chessboard_size: int = 8
