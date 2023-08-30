import os

__all__ = ['rename']

ZEROS: str = '0000000000'


def get_num_type(count: int, count_nums: int) -> str:
    count_len = int(str(count).__len__())
    if count_len < count_nums:
        return f'{ZEROS[:count_nums - count_len]}{count}'
    else:
        return str(count)


def rename(wanted_name: str, count_nums: int, extension_old: str, extension_new: str, diapazon: list):
    count: int = 0
    list_files = os.listdir(os.getcwd())

    for file in list_files:
        if extension_old in file:
            count += 1
            convert_count = get_num_type(count, count_nums)
            cut_name = file[diapazon[0]:diapazon[1] + 1]
            new_name_file = f'{cut_name}{wanted_name}{convert_count}{extension_new}'
            os.rename(file, new_name_file)
