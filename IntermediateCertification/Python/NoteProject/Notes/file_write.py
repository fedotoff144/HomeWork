from note import note

note = note()


def write_csv():
    file = 'Notes.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{note[0]};{note[1]};{note[2]};{note[3]}\n')
