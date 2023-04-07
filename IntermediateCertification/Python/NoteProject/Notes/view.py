import repository
import file_output


def menu():
    print('\nCommands for your choice\n************************')
    print(
        f'1 - add new note\n2 - preview all notes\n3 - update note\n4 - delete note\n0 - '
        f'exit\n********************************')
    command = input('Enter number for command please: ')
    match command:
        case '1':
            repository.write_csv()
        case '2':
            file_output.file_output()
        case '3':
            repository.count_lines_in_file()
            print('update')
        case '4':
            repository.delete(repository.find_note())
            print('note deleted')
        case '0':
            print('Good Buy!')
        case _:
            print(f'Sorry I don\'t know this command {command!r}')

    return command
