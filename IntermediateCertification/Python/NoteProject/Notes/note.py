import datetime


def note():
    note = []

    note.append(id(note))
    header = input('Enter header for note please: ')
    note.append(header)
    body_note = input('Enter note please: ')
    note.append(body_note)
    note.append(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y"))

    return note
