#!/usr/bin/python3
""" printing a text """


def text_indentation(text):
    """ This method prints a text with 2 new lines after each of these
    characters: ., ? and : and there should be no space at the begining
    or at the end of each printed line.

    Args:
        text (str): parameter

    Raises:
        TypeError: if text is not a str

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    check = 1
    for char_reader in text:
        if check != 0 and char_reader == ' ':
            continue
        check = 0
        print(char_reader, end="")
        if char_reader in [':', '?', '.']:
            check = 1
            print("\n")
