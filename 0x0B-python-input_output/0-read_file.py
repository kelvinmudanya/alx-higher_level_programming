#!/usr/bin/python3
""" method that reads a text file """


def read_file(filename=""):
    """ method definition
    Args:
        filename (str): the file passed to read
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
