# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину
# каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае
# отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = 6
b = 6
c = 12
message = 'Triangle doesn\'t exist'

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    if a == b == c:
        message = 'Triangle is equilateral'
    elif (a == b) or (b == c) or (c == a):
        message = 'Triangle is isosceles'
    else:
        message = 'Triangle is scalene'

print(message)