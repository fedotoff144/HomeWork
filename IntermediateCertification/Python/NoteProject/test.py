# Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания
import datetime
#
# note_id = 1
#
#
# def note():
#     note = []
#     global note_id
#
#     note.append(note_id)
#     header = input('Enter header for note, please: ')
#     note.append(header)
#     body_note = input('Enter note pleas: ')
#     note.append(body_note)
#     note.append(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y"))
#     note_id += 1
#     return note
#
#
# def write_csv():
#     file = 'Notes.csv'
#     with open(file, 'a', encoding='utf-8') as data:
#         data.write(f'{note[0]};{note[1]};{note[2]};{note[3]}\n')
#
#
# def read_all_notes():
#     with open('Notes.csv') as data:
#         data.read()


# def menu():
#     print('Commands for your choice\n************************')
#     print(
#         f'1 - add new note\n2 - preview all notes\n3 - update note\n4 - delete note\n********************************')
#     command = int(input('Enter number for command please: '))
#     match command:
#         case 1:
#             write_csv()
#         case 2:
#             read_all_notes()
#         case 3:
#             print('update')
#         case 4:
#             print('delete')
#         case 0:
#             print('Good Buy!')
#         case _:
#             print(f'Sorry I don\'t know this command {command!r}')
#
#
# menu()
