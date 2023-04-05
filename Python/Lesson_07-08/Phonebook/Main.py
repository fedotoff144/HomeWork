from os.path import exists
from View import menu_choise
from CSV_crate import csv_crate

path = 'Phonebook.csv'
valid = exists(path)

if not valid:
    csv_crate()

menu_choise()
