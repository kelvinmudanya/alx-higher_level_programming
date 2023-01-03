#!/usr/bin/python3
""" division method """


def matrix_divided(matrix, div):
    """ This method divides a  matrix (list of list) by a number passed in div
    there is certain conditions specially the type int or float as a must. And
    the same size between the list rows.

    Args:
        matrix (int or float): a list of list passed as first parameter
        div (int or float): must be a number and is the second parameter

    Raises:
        TypeError: if matrix is not a list of integers or floats
        TypeError: if each row of the matrix are not the same size
        TypeError: if parameter div is not an integer or a float
        ZeroDivisionError: if div is equal to zero

    Returns:
        new_matrix: a new list of lists with the division result rounded two
        decimal places
    """
    new_matrix = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(message)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(message)
        if len(row) != len(matrix[0]):
            raise TypeError(message2)

        for numbers in row:
            if type(numbers) not in (int, float):
                raise TypeError(message)

    return [[round(numbers / div, 2) for numbers in row] for row in matrix]
