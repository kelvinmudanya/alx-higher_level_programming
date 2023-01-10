#!/usr/bin/python3
""" Method to know is it or not an instance """


def is_same_class(obj, a_class):
    """ is same class definition
    Args:
        obj: an object
        a_class: a type class to chceck
    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False
    """
    return type(obj) is a_class
