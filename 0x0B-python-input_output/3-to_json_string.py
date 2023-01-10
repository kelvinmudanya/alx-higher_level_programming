#!/usr/bin/python3
""" method that writes a string to a text file """


def write_file(filename="", text=""):
    """ write_file definition
    Args:
        filename(str): the passed file to write in
        text (str): the string to write  in the passed file
    """
    with open(filename, encoding='utf-8', mode='w') as file:
        return file.write(text)
