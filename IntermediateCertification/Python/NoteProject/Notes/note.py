import datetime
import io


def note():
    note = []

    header = input('Enter header for note please: ')
    note.append(header)
    body_note = input('Enter note please: ')
    note.append(body_note)
    note.append(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y"))

    return note


def set_note_id():
    note_id = 0
    with io.open('Notes.csv', encoding='utf-8') as file:
        for line in file:
            split_string = line.split(';')
            if int(split_string[0].isdigit()) <= note_id:
                note_id += 1
            else:
                continue

    return note_id


def create_full_note(note, note_id):
    note.insert(0, note_id)
    return note

