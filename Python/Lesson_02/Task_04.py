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

for i in range(-n, n+1):
    array.append(int(i))

print(array)

m = input('Enter index: ')
second_arr = []
for i in m:
    if i != ' ':
        second_arr.append(int(i))

temp = 1
for i in second_arr:
    for j in array:
        if j == array[i]:
            temp *= j

print(temp)





# def createArray():
#     n = int(input('Enter n: '))
#     array = []
#     for i in range(-n, n+1):
#         array.append(int(i))
#     print(array)
#     return array


# def findWithIndex(array: list):
#     m = input('Enter index: ')
#     second_arr = []
#     for i in m:
#         if i != ' ':
#             second_arr.append(int(i))

#     temp = 1

#     for i in second_arr:
#         for j in array:
#             if j == array[i]:
#                 temp *= j

#     print(temp)

# findWithIndex(createArray())
