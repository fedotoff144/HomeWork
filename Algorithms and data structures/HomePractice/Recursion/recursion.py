# recursion function

def recurs_func(n):
    if n != 1:
        return n * recurs_func(n - 1)
    return 1


print(recurs_func(7))
