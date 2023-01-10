#!/usr/bin/python3
""" method to add attributes """


def add_attribute(object, name, value):
    """ method
    Raises:
        TypeError: if cant set an attribute
    """
    if hasattr(object, "__dict__"):  # hasattr check if object has attributes
        setattr(object, name, value)  # sets value of the attribute of an obj
    else:
        raise TypeError("can't add new attribute")
