# Task 5

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]



def Fibonachi(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return Fibonachi(n-1) + Fibonachi(n-2)

def FibonachiNegative(n):
    if n ==-1:
        return 1
    elif n == -2:
        return -1
    else:
        return FibonachiNegative(n+2) - FibonachiNegative(n+1)

list = []
k = int(input('Введите число К: '))
for e in range(-k,0):
    list.append(FibonachiNegative(e))
for e in range(0,k+1):
    list.append(Fibonachi(e))
print(list)