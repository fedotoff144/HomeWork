# finding a sum using recursion

my_arr = [1, 2, 3, 4, 5, 6]


def recurs_sum(arr: list) -> int:
    if len(arr) != 0:
        return arr.pop() + recurs_sum(arr)
    return 0


print(recurs_sum(my_arr))
