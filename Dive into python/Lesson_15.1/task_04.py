import argparse


def transpose(matrix):
    """
    Transposes a given matrix.

    :param matrix: List of lists representing the matrix.
    :return: Transposed matrix.
    """
    if len(matrix) == 1:
        return matrix

    result = []
    length_element = len(matrix[0])  # Assuming all rows have the same length
    for i in range(length_element):
        temp_lst = [row[i] for row in matrix]
        result.append(temp_lst)
    return result


def main():
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Transpose a matrix.')

    # Add the argument for the matrix
    my_parser.add_argument('Matrix', metavar='matrix', type=list, nargs='+',
                           help='The matrix to transpose')

    # Execute parse_args()
    args = my_parser.parse_args()

    # Flatten the list of lists into a single list
    flattened_matrix = [item for sublist in args.Matrix for item in sublist]

    # Reshape the flattened list back into a matrix
    matrix = [flattened_matrix[n:n + len(args.Matrix[0])] for n in
              range(0, len(flattened_matrix), len(args.Matrix[0]))]

    # Call the transpose function with the reshaped matrix
    result = transpose(matrix)

    # Print the result
    print(result)


if __name__ == '__main__':
    main()

#
# import argparse
#
#
# def key_params(**kwargs) -> dict:
#     """
#     This function takes keyword arguments, attempts to use them as keys in a dictionary,
#     converting non-hashable values to strings to ensure they can be used as dictionary keys.
#
#     :param kwargs: Keyword arguments to process.
#     :return: A dictionary with keys being the hashable versions of the input values and values being the original keys.
#     """
#     result_dict = {}
#     for key, value in kwargs.items():
#         try:
#             hash(value)
#         except TypeError:
#             value = str(value)
#         result_dict[value] = key
#     return result_dict
#
#
# def main():
#     # Create the parser
#     my_parser = argparse.ArgumentParser(description='Process some keywords.')
#
#     # Add the arguments
#     my_parser.add_argument('Keywords',
#                            metavar='keyword',
#                            type=str,
#                            nargs='+',
#                            help='the keyword arguments to process')
#
#     # Execute parse_args()
#     args = my_parser.parse_args()
#
#     # Convert positional arguments to keyword arguments
#     kwargs = {arg.split('=')[0]: arg.split('=')[1] for arg in args.Keywords}
#
#     # Call the key_params function with the parsed keyword arguments
#     result = key_params(**kwargs)
#
#     # Print the result
#     print(result)
#
#
# if __name__ == '__main__':
#     main()
