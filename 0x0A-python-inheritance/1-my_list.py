#!/usr/bin/python3
""" Class MyList inherit from list"""


class MyList(list):
    """ class my list"""
    def print_sorted(self):
        """ prints a sorted list (ascending sort) """
        print(sorted(self))
