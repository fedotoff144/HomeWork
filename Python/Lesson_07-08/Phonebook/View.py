def menu_choise():
    print(f'1 - Добавление контакта\n2 - Вывод книги контактов\n0 - Выход из прогаммы')
    command = int(input('Введите цифру меню: '))
    match command:
        case 1:
            from File_write import write_csv
            from File_write import write_txt
            write_csv()
            write_txt()
        case 2:
            from Output import read_file
            read_file()
        case 0:
            print("Пока!")
        case _:
            print(f"Извините, команда {command!r} отсутствует в списке")


def get_contact():
    contact = []
    last_name = input('Введите фамилию: ')
    contact.append(last_name)
    name = input('Введите имя: ')
    contact.append(name)
    phone_numb = ''

    while True:
        try:
            phone_numb = input('Введите номер телефона: ')
            if len(phone_numb) != 11:
                print('В номере телефона должно быть 11 цифр!')
            else:
                phone_numb = int(phone_numb)
                break
        except:
            print('Номер должен состоять тольо из цифр!')
    contact.append(phone_numb)
    extra = input('Введите дополнительное описание: ')
    contact.append(extra)
    return contact
