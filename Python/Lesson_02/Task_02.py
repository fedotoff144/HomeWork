# Task 2

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input("Enter number :"))
arr = []
x = 1

for i in range(0, n+1):
    if i == 0:
        arr.append(1)
        continue
    x *= i
    arr.append(x)

print(arr)
