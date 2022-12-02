# Task 5

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]


def listOfFuctorials():
    number = int(input('Введите число N, для получения массива факториалов от 0 до N: '))
    fuctorials = []

    def fuctorial(n):
        if n == 0: 
            fuctorials.append(1)
            return 1
        value = n * fuctorial(n - 1)
        fuctorials.append(value)
        return value
        
    fuctorial(number)
    print(fuctorials)

listOfFuctorials()



def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def not_fib(n):
    if n ==-1:
        return 1
    elif n == -2:
        return -1
    else:
        return not_fib(n+2) - not_fib(n+1)

list = []
k = int(input('Введите число К: '))
for e in range(-k,0):
    list.append(not_fib(e))
for e in range(0,k+1):
    list.append(fib(e))
print(list)