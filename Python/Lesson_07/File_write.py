from View import get_contact as gc


info = gc()


def write_csv():
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')


def write_txt():
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n')
