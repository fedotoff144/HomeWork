# Task 4

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Enter n: '))
arr = []

for i in range(-n, n+1):
    arr.append(i)

print(arr)

m = input('Enter index: ')
ind = []
for i in m:
    if i != ' ':
        ind.append(i)

print(ind)

for i in ind:
    print(arr.index(i))
