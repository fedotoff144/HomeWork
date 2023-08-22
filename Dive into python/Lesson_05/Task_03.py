"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def fibonacci_func(n):
    fib = 3
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, n):
            fib = fib - 2 + fib - 1
            yield fib


fib_num = fibonacci_func(5)
print(next(fib_num))
print(next(fib_num))
print(next(fib_num))
print(next(fib_num))
