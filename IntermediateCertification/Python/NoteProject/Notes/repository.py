import note
import io


def write_csv(new_note, id_note):
    nt = note.create_full_note(new_note, id_note)
    file = 'Notes.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{nt[0]};{nt[1]};{nt[2]};{nt[3]}\n')


def find_note(note_id):
    with io.open('Notes.csv', encoding='utf-8') as file:
        for line in file:
            split_string = line.split(';')
            if split_string[0] == note_id:
                return split_string
            else:
                continue


def delete(note_id):
    with open('Notes.csv', 'r+') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            split_line = line.split(';')
            if split_line[0] != note_id:
                f.write(line)
        f.truncate()
