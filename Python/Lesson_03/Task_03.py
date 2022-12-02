# Task 3

# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19


import random
from decimal import Decimal

def num_list(n):
    for i in range(n):
        list.append(round(random.uniform(1,10),2))
    return list

def difference():
    for i in range(n):
        list_diff.append(list[i]%1)
    diff = (max(list_diff)) - (min(list_diff))
    return round(diff,2)

list = []
list_diff = []
n = int(input('Введите размер списка: '))
print(f'{num_list(n)} => {difference()}')
