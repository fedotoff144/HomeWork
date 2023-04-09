import datetime
import io


def note():
    new_note = []

    header = input('Enter header for note please: ')
    new_note.append(header)
    body_note = input('Enter note please: ')
    new_note.append(body_note)
    new_note.append(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y"))

    return new_note


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


def create_full_note(note_body, note_id):
    note_body.insert(0, note_id)
    return note_body
