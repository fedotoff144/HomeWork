from os.path import exists
import view
import file_create as fc

path = 'Notes.csv'
valid = exists(path)

if not valid:
    fc.csv_create()

# while view.menu() != '0':
#     view.menu()

view.menu()
