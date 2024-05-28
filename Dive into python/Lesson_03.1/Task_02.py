"""
В большой текстовой строке text подсчитать количество встречаемых слов и
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
(после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов.
Слова выведите в обратном алфавитном порядке.

Пример

На входе:
text = 'Hello world. Hello Python. Hello again. Don't give up and hold on!'

На выходе:
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
"""
# text = "Hello world. Hello Python. Hello again. Don't give up and hold on!"
text = 'Hello world. Hello Python. Hello again. Python. Python. Python'
text = text.replace('\'', ' ')

clean_text = ''.join([item for item in text if item.isalpha() or item == ' ']).split()
result_lst = []
for word in clean_text:
    temp_tuple = (word, clean_text.count(word))
    if temp_tuple not in result_lst:
        result_lst.append(temp_tuple)

print(result_lst)

sorted_lst = []
for item in result_lst:
    max_item = max(*result_lst)
    sorted_lst.append(max_item)
    result_lst.remove(max_item)

print(sorted_lst)

