from prettytable import PrettyTable


def read_file():
    with open("Phonebook.csv", 'r') as data:
        table = PrettyTable(["Фамилия", "Имя", "Телефон", "Описание"])
        for line in data:
            row = line.split(';')
            table.add_row(row)
    table.del_row(0)
    print(table)
