# Task 2

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def find_myl(n):
    lst = []
    i = 2

    while i <= n:
        if n % i == 0:
            lst.append(i)
            n //= i
        else:
            i += 1

    return print(lst)


n = int(input("Enter natural namber N: "))

find_myl(n)
