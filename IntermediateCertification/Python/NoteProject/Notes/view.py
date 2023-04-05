import repository
import file_output



def menu():
    print('\nCommands for your choice\n************************')
    print(
        f'1 - add new note\n2 - preview all notes\n3 - update note\n4 - delete note\n0 - exit\n********************************')
    command = input('Enter number for command please: ')
    match command:
        case '1':
            repository.write_csv()
        case '2':
            file_output.file_output()
        case '3':
            print('update')
        case '4':
            print('delete')
        case '0':
            print('Good Buy!')
        case _:
            print(f'Sorry I don\'t know this command {command!r}')

    return

