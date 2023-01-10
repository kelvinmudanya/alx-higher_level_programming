#!/usr/bin/python3
""" method that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ method append_write definition
    Args:
        filename (str): the passed file to read and append to
        text (str): the string to append on the file
    """
    with open(filename, encoding='utf-8', mode='a') as file:
        return file.write(text)
