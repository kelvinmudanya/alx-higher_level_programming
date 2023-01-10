#!/usr/bin/python3
""" method to decode """
import json


def from_json_string(my_str):
    """ definition to decode method
    Args:
        my_str (str): to decode from json string to python strcuture
    Returns:
        an object (python data structure)
    """
    return json.loads(my_str)
