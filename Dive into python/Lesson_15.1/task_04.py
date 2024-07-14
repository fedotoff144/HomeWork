import argparse


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
    parser = argparse.ArgumentParser(description='Task for intermediate certification')
    parser.add_argument('-m', '--matrix', help='Enter matrix')
    args = parser.parse_args()
    print(type(args))
    return transpose(args)


if __name__ == '__main__':
    print(parse())
