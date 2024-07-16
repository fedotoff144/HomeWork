"""
- Добавьте к задаче логирование ошибок и полезной информации.
- Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
import logging
import argparse
import ast


FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} запуск функции "{funcName}()". ' \
         'Статус работы: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.DEBUG,
                    filename='log_task_01.log', filemode='a', encoding='utf-8')
logger = logging.getLogger('task_1.py')


def transpose(matrix):
    if len(matrix) == 1:
        return matrix

    result = []
    length_row = len(matrix[0])
    for i in range(length_row):
        temp_lst = [row[i] for row in matrix]
        result.append(temp_lst)

    return result


def parse():
    parser = argparse.ArgumentParser(description='Task for intermediate certification',
                                     prog='transpose', epilog='Returns the transposed matrix')
    try:
        parser.add_argument('-m', '--matrix', metavar='MATRIX', type=str, nargs=1,
                            default='[[1,2,3],[1,2,3],[1,2,3]]',
                            help='pass matrix as a string without spaces, for example: [[1,2,3],[1,2,3],[1,2,3]]')
        args = parser.parse_args()
        matrix = ast.literal_eval(*args.matrix)
        result = transpose(matrix)
        logger.info('OK')
        return result
    except Exception as e:
        logger.error(f'ERROR {e}')


if __name__ == '__main__':
    print('OK...' if parse() else 'ERROR!')

# command for run
# python task_01.py -m [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
