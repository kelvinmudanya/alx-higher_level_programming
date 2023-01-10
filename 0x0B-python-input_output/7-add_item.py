#!/usr/bin/python3
""" json method that writes an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ json method definition
    Args:
        my_obj (str): to write
        filename (str): file to write in using json representation
    """
    with open(filename, encoding='utf-8', mode='w') as file:
        json.dump(my_obj, file)
