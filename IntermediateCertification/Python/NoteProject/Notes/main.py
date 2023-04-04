import note
import create_csv as cc
import file_write as fw
from os.path import exists
import file_output as fr

path = 'Notes.csv'
valid = exists(path)

if not valid:
    cc.csv_create()

note.note()
fw.write_csv()
fr.file_read()