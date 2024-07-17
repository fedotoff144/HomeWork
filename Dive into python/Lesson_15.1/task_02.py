"""
- Добавьте к задаче логирование ошибок и полезной информации.
- Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
import argparse
import ast
import logging


FORMAT = '{levelname:<6}-  {asctime}. line: {lineno:03d}. Status: {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='log_task_02.log', filemode='a',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('task_02.py')


class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        lst_win_nums = []
        for i in self.list1:
            if i in self.list2:
                lst_win_nums.append(i)
                self.list2.remove(i)
        if len(lst_win_nums) > 0:
            return f'Совпадающие числа: {lst_win_nums}\n' \
                   f'Количество совпадающих чисел: {len(lst_win_nums)}'
        else:
            return 'Совпадающих чисел нет.'

    def __str__(self):
        return f'class name: LotteryGame, lottery ticket: {self.list1}, win numbers: {self.list2}'

    def __repr__(self):
        return f'LotteryGame({self.list1}, {self.list2})'


def parse():
    try:
        parser = argparse.ArgumentParser(description='Task for intermediate certification',
                                         prog='LotteryGame',
                                         epilog='creates the LotteryGame class')
        parser.add_argument('-n', '--name', metavar='NAME_OF_CLASS', nargs=1, type=str,
                            help='Enter name of class, for example: LotteryGame')
        parser.add_argument('-lt', '--lottery_ticket', metavar='LOTTERY_TICKET', nargs=1, type=str,
                            help='pass list of numbers in lottery ticket as a string without spaces, for example: [1,2,3,4,5,6]')
        parser.add_argument('-wn', '--win_nums', metavar='WIN_NUMS', nargs=1, type=str,
                            help='pass list of win numbers as a string without spaces, for example: [1,2,3,4,5,6]')
        args = parser.parse_args()

        class_name = globals()[str(*args.name)]
        lottery_ticket = ast.literal_eval(*args.lottery_ticket)
        win_nums = ast.literal_eval(*args.win_nums)

        result = class_name(lottery_ticket, win_nums)
        # print(result.compare_lists())
        logger.info(f'OK. Result: {result}')
        return result
    except Exception as e:
        logger.error(f'Error! {args}')


if __name__ == '__main__':
    print('OK...' if parse() else 'ERROR!')

# command for run
# python task_02.py -c LotteryGame -l1 [3,12,8,41,7,21,9,14,5,30] -l2 [9,5,6,12,14,22,17,41,8,3]
