# Task 1

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

num = input("Enter number: ")
sum = 0

for i in str(num):
    if (i != '.') and (i != ','):
        sum += int(i)

print(sum)
