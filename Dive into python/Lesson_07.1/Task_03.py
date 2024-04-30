"""
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.

"""
import random

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANTS = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'
]


def gen_name():
    length_name = random.randint(4, 7)
    vowels_quantity = length_name // 2
    consonants_quantity = length_name - vowels_quantity

    list_letters = random.sample(VOWELS, vowels_quantity) + \
                   random.sample(CONSONANTS, consonants_quantity)
    random.shuffle(list_letters)
    pseudonym = ''.join(list_letters).capitalize()

    with open('pseudonyms.txt', 'a', encoding='utf-8') as f:
        f.write(pseudonym + '\n')


gen_name()
