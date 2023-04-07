import note
import re
import io


def write_csv():
    nt = note.create_full_note(note.note(),note.set_note_id())
    file = 'Notes.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{nt[0]};{nt[1]};{nt[2]};{nt[3]}\n')


def count_lines_in_file():
    note_id = 1
    with io.open('Notes.csv', encoding='utf-8') as file:
        for line in file:
            split_string = line.split(';')
            while int(split_string[0]) <= note_id:
                note_id += 1


def find_note():
    find_id = input('Enter id note please : ')
    return find_id


def update(find_id):
    find_id = 0

    return ' '


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
