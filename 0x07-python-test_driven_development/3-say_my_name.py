#!/usr/bin/python3
""" Printing names and last names """


def say_my_name(first_name, last_name=""):
    """ This method prints the first name and the last name

    Args:
        first_name (str): first parameter string type
        last_name (str): second parameter string type with empty str default

    Raises:
        TypeError: if first_name and last_name are not strings

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
