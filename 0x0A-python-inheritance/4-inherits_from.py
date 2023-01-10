#!/usr/bin/python3
""" method to check inheritance """


def inherits_from(obj, a_class):
    """ method defitinion returns True or False """
    return isinstance(obj, a_class) and type(obj) is not a_class
