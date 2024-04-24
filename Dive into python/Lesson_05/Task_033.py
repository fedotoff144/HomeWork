"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def fib_gen(n):
    a = 0
    b = 1
    for i in range(1, n + 1):
        a, b = b, a + b
        yield b


iter_fib = iter(fib_gen(10))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib))
print(next(iter_fib, 'stop generation'))
