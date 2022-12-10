# Task 1

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


my_string = input('Введите текст: ')
serch_text = input('Введите ключевоые буквы для удаления слов: ')

my_li = my_string.split()
my_li = list(filter(lambda el: not serch_text in el, my_li))
my_string = ' '.join(my_li)
print(my_string)
