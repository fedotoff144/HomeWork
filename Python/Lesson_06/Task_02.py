# Task 2

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

num = input("Enter number: ")


def symbol(i):
    if (i == '.') or (i == ','):
        return 0
    else:
        return int(i)


print(sum(list(map(symbol, num))))
