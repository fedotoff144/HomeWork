# Task 5
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from cmath import sqrt

x1 = int(input('Enter first point x: '))
y1 = int(input('Enter first point y: '))
x2 = int(input('Enter second point x: '))
y2 = int(input('Enter second point y: '))

print(sqrt((x2-x1)**2+(y2-y1)**2))