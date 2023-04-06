import note
import re


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


def find_note():
    find_id = input('Enter id note please : ')
    return find_id


def delete(find_id):
    pattern = re.compile(re.escape(find_id))
    with open('Notes.csv', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            f.truncate()
