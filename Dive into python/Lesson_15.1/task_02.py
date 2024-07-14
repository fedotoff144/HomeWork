"""
- Добавьте к задаче логирование ошибок и полезной информации.
- Также реализуйте возможность запуска из командной строки с передачей параметров.
"""


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


if __name__ == '__main__':
    list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
    game = LotteryGame(list1, list2)
    game.compare_lists()
