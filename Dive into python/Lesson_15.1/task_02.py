"""
- Добавьте к задаче логирование ошибок и полезной информации.
- Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
import logging, argparse


FORMAT = ''
logging.basicConfig(format=FORMAT, style='{', filename='log_task_01.log', filemode='a', encoding='utf-8')
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
            return f'Совпадающие числа: {lst_win_nums}\n'\
                   f'Количество совпадающих чисел: {len(lst_win_nums)}'
        else:
            return 'Совпадающих чисел нет.'


def parse():
    parser = argparse.ArgumentParser(description='Task for intermediate certification',
                            prog='LotteryGame',
                            epilog='creates the LotteryGame class')
    parser.add_argument('-c', '--class', metavar='CLASSNAME', nargs=1, type=str,
                        help='Enter class name, for example: LotteryGame')
    parser.add_argument('-l1', '--list1', metavar='LIST1', nargs=1, type=str,
                        help='pass list of numbers as a string without spaces, for example: [1,2,3,4,5,6]')
    parser.add_argument('-l2', '--list2', metavar='LIST2', nargs=1, type=str,
                        help='pass list of numbers as a string without spaces, for example: [1,2,3,4,5,6]')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
    # game = LotteryGame(list1, list2)
    # game.compare_lists()
    parse()

# command for run
# python task_02.py -c LotteryGame -l1 [3,12,8,41,7,21,9,14,5,30] -l2 [9,5,6,12,14,22,17,41,8,3]