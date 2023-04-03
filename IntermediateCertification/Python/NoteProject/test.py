# Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания
import datetime

def note():
    note = []

    header = input('Enter header for note, please: ')
    note.append(header)
    body_note = input('Enter note pleas: ')
    note.append(body_note)
    note.append(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y"))
    print(note[1])

note()
