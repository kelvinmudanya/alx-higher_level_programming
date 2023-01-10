#!/usr/bin/python3
""" Pascal's Triangle method """


def pascal_triangle(n):
    """ pascal triangle definition returns a list of lists of integers """
    list_of_lists = []
    row = []
    prev_row = []

    if n <= 0:
        return []

    for i in range(0, n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and prev_row[j - 1] +
               prev_row[j] or 1 for j in range(0, i)]
        prev_row = row
        list_of_lists += [row]
    return list_of_lists[1:]
