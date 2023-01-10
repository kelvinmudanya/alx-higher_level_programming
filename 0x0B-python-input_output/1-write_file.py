#!/usr/bin/python3
""" method that returns the number of lines od a text file """


def number_of_lines(filename=""):
    """ method num of lines
    Args:
        filename (str): the passed file
    """
    with open(filename, encoding='utf-8') as file:
        return len(file.readlines())
