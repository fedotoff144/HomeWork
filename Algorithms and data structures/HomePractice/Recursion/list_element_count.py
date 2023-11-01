# counting of list element by recursion

my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13]


def func_count(arr:list):
    if len(arr) != 0:
        arr.pop()
        return 1 + func_count(arr)
    return 0


print(func_count(my_arr))