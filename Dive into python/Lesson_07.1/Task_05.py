"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.

"""


def mix_files(nums, names):
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


mix_files('fill_out.txt', 'pseudonyms.txt')
