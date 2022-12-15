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
