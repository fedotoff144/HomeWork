import note


def write_csv():
    nt = note.note()
    file = 'Notes.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{nt[0]};{nt[1]};{nt[2]};{nt[3]}\n')


def read_all_notes():
    with open('Notes.csv') as data:
        data.read()


def update():
    id_search = str(input('Enter note id to search: '))

    return ' '

def find():

    return ' '


def delete():
    return ' '
