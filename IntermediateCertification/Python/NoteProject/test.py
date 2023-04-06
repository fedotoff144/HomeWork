import io
import re


# def read_all_notes():
#     with open('Notes.csv') as data:
#         data.read()


a = '140162872638912'
#
# # if a in read_all_notes():
# #     print('ok')
#
with io.open('Notes.csv', encoding='utf-8') as file:
    for line in file:
        if a in line:
            print(line)



with open('f.txt') as f:
    lines = f.readlines()

str = 'Hello'
pattern = re.compile(re.escape(str))
with open('f.txt', 'w') as f:
    for line in lines:
        result = pattern.search(line)
        if result is None:
            f.write(line)

# Или почти тоже самое, но в один проход (но я за первый вариант)
#
# #!/usr/bin/env python3

import re

str = 'Hello'
pattern = re.compile(re.escape(str))
with open('f.txt', 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        result = pattern.search(line)
        if result is None:
            f.write(line)
        f.truncate()

