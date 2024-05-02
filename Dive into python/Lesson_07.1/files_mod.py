import random
from pathlib import Path

__all__ = ['merging_files', 'sorting_files', 'gen_name', 'rename_group_files',
           'filling_out_file']

__VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
__CONSONANTS = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'
]


def filling_out_file(file_name: str, count_line: int):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(count_line):
            f.write(f'{random.randint(-1000, 1001)}|' \
                    f'{random.uniform(-1000, 1001)}\n')


def rename_group_files(wanted_name: str, count_nums: int, extension_old: str,
                       extension_new: str, diapazon: list):
    # get home directory
    pwd = Path.cwd()
    # set counter changed files
    count_files = 1

    slice_extension = len(extension_old)

    for obj in pwd.iterdir():
        if str(obj)[-slice_extension:] == extension_old:
            # set counter to needed format
            count_str = '0' * (count_nums - len(str(count_files))) + \
                        str(count_files)
            # get slice of old file name
            old_file_name = obj.name[diapazon[0]:diapazon[1]]
            # assemble the name and rename the object
            new_file_name = old_file_name + wanted_name + count_str + \
                            extension_new
            obj.rename(new_file_name)
            count_files += 1


def gen_name(quantity: int):
    for _ in range(quantity):
        length_name = random.randint(4, 7)
        vowels_quantity = length_name // 2
        consonants_quantity = length_name - vowels_quantity

        list_letters = random.sample(__VOWELS, vowels_quantity) + \
                       random.sample(__CONSONANTS, consonants_quantity)
        random.shuffle(list_letters)
        pseudonym = ''.join(list_letters).capitalize()

        with open('pseudonyms.txt', 'a', encoding='utf-8') as f:
            f.write(pseudonym + '\n')


def sorting_files(path):
    home_dir = Path(path)

    # create necessary folders for sorting
    if not Path(home_dir / 'pictures').exists():
        Path.mkdir(home_dir / 'pictures')
    if not Path(home_dir / 'video').exists():
        Path.mkdir(home_dir / 'video')
    if not Path(home_dir / 'text').exists():
        Path.mkdir(home_dir / 'text')
    if not Path(home_dir / 'music').exists():
        Path.mkdir(home_dir / 'music')

    for obj in home_dir.rglob('*'):
        if obj.is_file():
            if obj.name.endswith('.jpg') or obj.name.endswith('.png'):
                obj.replace(home_dir / 'pictures' / obj.name)
            if obj.name.endswith('.mp4') or obj.name.endswith('.avi'):
                obj.replace(home_dir / 'video' / obj.name)
            if obj.name.endswith('.txt') or obj.name.endswith('.csv') \
                    or obj.name.endswith('.doc') or obj.name.endswith('.docx') \
                    or obj.name.endswith('.pdf'):
                obj.replace(home_dir / 'text' / obj.name)
            if obj.name.endswith('.mp3') or obj.name.endswith('.aac'):
                obj.replace(home_dir / 'music' / obj.name)


def merging_files(nums, names):
    with (
        open(nums, 'r', encoding='utf-8') as f1,
        open(names, 'r', encoding='utf-8') as f2,
        open('result.txt', 'a', encoding='utf-8') as f3
    ):
        marker_f1 = 0  # marker for stop loop
        marker_f2 = 0  # marker for stop loop
        while True:
            line_f1 = f1.readline()
            line_f2 = f2.readline()

            if not line_f1 and marker_f2 != 0 or not line_f2 and marker_f1 != 0:
                break
            if not line_f1 and marker_f2 == 0:
                marker_f1 += 1
                f1.seek(0)
                line_f1 = f1.readline()
            if not line_f2 and marker_f1 == 0:
                marker_f2 += 1
                f2.seek(0)
                line_f2 = f2.readline()

            # clear lines and perform calculations
            line_f1 = line_f1.replace('\n', '').split('|')
            line_f2 = line_f2.replace('\n', '')
            res_mult = int(line_f1[0]) * float(line_f1[1])

            # writing strings into file f3
            if res_mult <= 0:
                line = f'{line_f2.lower()} {res_mult * (-1)}\n'
                f3.write(line)
            if res_mult > 0:
                line = f'{line_f2.upper()} {int(res_mult)}\n'
                f3.write(line)


if __name__ == '__main__':
    merging_files('fill_out.txt', 'pseudonyms.txt')

    sorting_files('H:\SamsungPhone')

    gen_name(5)

    rename_group_files('_note_', 4, '.txt', '.txt', [0, 4])

    filling_out_file('fill_out.txt', 10)
