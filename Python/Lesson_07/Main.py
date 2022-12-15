from os.path import exists
from CSV_crate import csv_crate
from File_write import write_csv
from File_write import write_txt

path = 'Phonebook.csv'
valid = exists(path)

if not valid:
    csv_crate()

write_csv()
write_txt()