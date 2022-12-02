# Task 2

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



from random import randint

n = int(input('Введите размер списка: '))

lst = []

for i in range(n):
    lst.append(randint(1, 10))

length = n // 2
second_lst = []
for i in range(length if (len(lst) % 2 == 0) else length + 1):
    i = lst[i]*lst[-i-1]
    second_lst.append(i)

print(f'Общий список: {lst} \nРезультат перемножений: {second_lst}')
