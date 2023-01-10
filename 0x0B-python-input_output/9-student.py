#!/usr/bin/python3
""" class Student """


class Student:
    """ definition """
    def __init__(self, first_name, last_name, age):
        """ instantiation with
        Args:
            first_name (str): public instance attributes
            last_name (str): public instance attributes
            age (int): public instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method that retrieves a dictionary representation
        of a student instance """
        if isinstance(attrs, list) and ([isinstance(n, str)] for n in attrs):
            new_dictionary = {}
            for words in attrs:
                if words in self.__dict__:
                    new_dictionary[words] = self.__dict__[words]
            return new_dictionary

        return self.__dict__
