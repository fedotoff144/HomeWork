# Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания
import datetime


note_id = 1


def note():
    note = []
    global note_id

    note.append(note_id)
    header = input('Enter header for note, please: ')
    note.append(header)
    body_note = input('Enter note pleas: ')
    note.append(body_note)
    note.append(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y"))
    note_id += 1
    return note


note()
note()
note()
print(note()[0])
