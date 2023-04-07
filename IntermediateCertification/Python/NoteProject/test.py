import io
import re
import numpy as np


# def read_all_notes():
#     with open('Notes.csv') as data:
#         data.read()


# a = '140162872638912'
#
# # if a in read_all_notes():
# #     print('ok')
#
# with io.open('Notes.csv', encoding='utf-8') as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)

def set_note_id():
    note_id = 1
    with io.open('Notes.csv', encoding='utf-8') as file:
        for line in file:
            split_string = line.split(';')
            if int(split_string[0].isdigit()) <= note_id:
                note_id += 1
            else:
                continue

    return note_id

            # while split_string[0] <= note_id:
            #     note_id += 1

    # return print(note_id)


print(set_note_id())
#
#
# with open('f.txt') as f:
#     lines = f.readlines()
#
# str = 'Hello'
# pattern = re.compile(re.escape(str))
# with open('f.txt', 'w') as f:
#     for line in lines:
#         result = pattern.search(line)
#         if result is None:
#             f.write(line)

# Или почти тоже самое, но в один проход (но я за первый вариант)
#
# #!/usr/bin/env python3

# import re
#
# str = '1405563834561178560'
# pattern = re.compile(re.escape(str))
# with open('Notes.csv', 'r+') as f:
#     lines = f.readlines()
#     f.seek(0)
#     for line in lines:
#         result = pattern.search(line)
#         if result is None:
#             f.write(line)
#         f.truncate()
#
