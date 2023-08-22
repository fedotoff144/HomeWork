"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def fibonacci_func(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, b + a
            yield a


fib_num = fibonacci_func(10)
print(next(fib_num))
print(next(fib_num))
print(next(fib_num))
print(next(fib_num))
print(next(fib_num))
print(next(fib_num))
print(next(fib_num))
print(next(fib_num))
# print(next(fib_num)) # StopIteration

