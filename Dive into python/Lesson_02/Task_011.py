# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.


user_input = int(input('Enter number for convert: '))
CHECK = user_input
SYMBOLS_ARRAY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
COMMON_DIV = 16
result: list = []


while user_input > 0:
    result.insert(0, str(SYMBOLS_ARRAY[user_input % COMMON_DIV]))
    user_input //= COMMON_DIV


print(f'Original method hex(): {hex(CHECK)}')
print(f"Converter: 0x{''.join(result)}")
