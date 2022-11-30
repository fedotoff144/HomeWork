# Task 4
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (num и y).


num = int(input('Enter number: '))

if num == 1:
    print('Coordinates within x + ~, y + ~')
elif num == 2:
    print('Coordinates within x - ~, y + ~')
elif num == 3:
    print('Coordinates within x - ~, y - ~')
elif num == 4:
    print('Coordinates within x + ~, y - ~')
else:
    print('Try again')
