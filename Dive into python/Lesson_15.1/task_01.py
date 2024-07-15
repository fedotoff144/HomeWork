"""
- Добавьте к задаче логирование ошибок и полезной информации.
- Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
import logging
import argparse
import json
from typing import Callable
import os

# FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
#          'в строке {lineno:03d} функция "{funcName}()" ' \
#          'в {created} секунд записала сообщение: {msg}'
# logging.basicConfig(format=FORMAT, style='{',
#                     level=logging.INFO,
#                     filemode='a',
#                     filename='log_task_01.log',
#                     encoding='utf-8'
#                     )
# logger = logging.getLogger(__name__)
#
#
# def my_deco(func: Callable):
#     def wrapper(args):
#         try:
#             result = func(args)
#             result_dict = {'function name': func.__name__,
#                            'function arguments': [*args],
#                            'result': result
#                            }
#
#             data = []
#             for cur_dir, dirs, files in os.walk(os.getcwd()):
#                 if 'task_01_info.json' in files:
#                     with open('task_01_info.json', 'r+', encoding='utf-8') as f_json:
#                         data = json.load(f_json)
#
#             data.append(result_dict)
#             with open('task_01_info.json', 'w', encoding='utf-8') as f_json_write:
#                 json.dump(data, f_json_write)
#             logger.info(result_dict)
#         except Exception as e:
#             logger.error(e)
#
#         return None
#
#     return wrapper
#
#
# @my_deco
def transpose(matrix):
    if len(matrix) == 1:
        return matrix
    result = []
    length_element = len(matrix[1])
    for i in range(length_element):
        temp_lst = [line[i] for line in matrix]
        result.append(temp_lst)
    return result


def parse():
    parser = argparse.ArgumentParser(description='Task for intermediate certification',
                                     prog='transpose()',
                                     epilog='End of help')
    parser.add_argument('-m', '--matrix', default='[[1,2,3],[1,2,3],[1,2,3]]',
                        help='pass a list of format [[1,2,3],[1,2,3],[1,2,3]]')
    args = parser.parse_args()
    return transpose(args)


if __name__ == '__main__':
    # print('ok')
    # matrix = [[11, 21, 31],
    #           [41, 51, 61],
    #           [71, 81, 91]]
    # new_matrix = transpose(matrix)
    parse()
