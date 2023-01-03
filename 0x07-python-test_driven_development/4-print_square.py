#!/usr/bin/python3
""" Printing a square """


def print_square(size):
    """ This method prints a square with character #

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: If size is not an integer, less than zero and/or a float

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print("")
