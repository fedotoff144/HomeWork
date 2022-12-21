# Task 4

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Enter n: '))

array = []
[array.append(int(i)) for i in range(-n, n+1)]

print(array)

m = input('Enter index: ')

second_arr = []
[second_arr.append(int(i)) for i in m if i != ' ']

temp = 1
for i in second_arr:
    for j in array:
        if j == array[i]:
            temp *= j

print(temp)
