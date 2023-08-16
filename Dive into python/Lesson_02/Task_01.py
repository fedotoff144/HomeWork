# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.

my_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
           6: '6', 7: '7', 8: '8', 9: '9', 10: 'a',
           11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

user_num = int(input('Enter your number:  '))
process_num = user_num
HEX_DIV = 16
my_arr = []
res = ''

while process_num > 0:
    my_arr.insert(0, process_num % HEX_DIV)
    process_num //= HEX_DIV

for element in my_arr:
    res += str(my_dict.get(element))


print(hex(user_num))
print(res)
