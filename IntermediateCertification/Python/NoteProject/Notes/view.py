import repository
import file_output
import note


def menu():
    print('\nCommands for your choice\n************************')
    print(
        f'1 - add new note\n2 - preview all notes\n3 - update note\n4 - delete note\n0 - '
        f'exit\n********************************')
    command = input('Enter number for command please: ')
    match command:
        case '1':
            nt = note.note()
            id_nt = note.set_note_id()
            repository.write_csv(nt, id_nt)
            print('Note added!')
        case '2':
            file_output.file_output()
        case '3':
            note_id = input('Enter id note please: ')
            repository.delete(note_id)
            repository.write_csv(note.note(), note_id)
            print('Note updated')
        case '4':
            note_id = input('Enter id note please: ')
            repository.delete(note_id)
            print('Note deleted')
        case '0':
            print('Good Buy!')
        case _:
            print(f'Sorry I don\'t know this command {command!r}')

    return command
