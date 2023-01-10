#!/usr/bin/python3
""" method that reads n lines of a file """


def read_lines(filename="", nb_lines=0):
    """ read_lines definition
    Args:
        filename (str): the passed file
        nb_lines (int): the amount of lines to read
    """
    with open(filename, encoding='utf-8') as file:
        if nb_lines <= 0:
            print(file.read(), end='')  # the complete file
        for line_num, line in enumerate(file):
            if line_num >= nb_lines:
                break  # prints the n lines
            print(line, end='')
