import prettytable


def file_read():
    with open('Notes.csv', 'r') as data:
        table = prettytable.PrettyTable(['ID', 'Header', 'Note', 'Time create'])
        for line in data:
            row = line.split(';')
            table.add_row(row)
    table.del_row(0)
    print(table)
