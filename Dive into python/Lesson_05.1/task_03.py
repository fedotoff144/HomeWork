"""
Создайте функцию генератор чисел Фибоначчи fibonacci.

Пример использования.

На входе:
f = fibonacci()
for i in range(10):
    print(next(f))

На выходе:
0
1
1
2
3
5
8
13
21
34
"""


def fibonacci():
    a = 0
    b = 0
    while True:
        if a == 0:
            a, b = 1, 0
            yield 0
        if a == 1 and b == 0:
            a, b = 1, 1
            yield 1
        a, b = a + b, a
        yield a + b

f = fibonacci()

for _ in range(10):
    print(next(f))
