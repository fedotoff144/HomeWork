# Task 1

# Вычислить число c заданной точностью d
# Пример:

# при d = 0.001, π = 3.141
# Ввод: 0.01
# Вывод: 3.14
# Ввод: 0.001
# Вывод: 3.141


import math


d = input("Enter d: ")
temp = d.split('.').pop(1)

print(round(math.pi, len(temp)))
