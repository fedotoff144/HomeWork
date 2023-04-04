def csv_create():
    file = 'Notes.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'ID;Header;Note;Time create\n')
