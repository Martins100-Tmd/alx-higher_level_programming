#!/usr/bin/python3
"""Define a matrix dividing function."""


def matrix_divided(matrix, div):
    """matrix_divided initialized.

    Divides all elements of a matrix

    Args:
        matrix(list): a list of list of int and floats
        div(int): list of list divisor

    Raises:
        Note if matrix is not integer or floats, TypeError will be raised

        if each row of the matrix is not the same size TypeError will be raised

        Divisor must be an integer otherwise TypeError will be raised

    All element will be rounded up to 2 decimal places.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: rounded(x / div, 2), row)) for row in matrix])
