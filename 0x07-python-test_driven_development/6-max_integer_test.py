#!/usr/bin/python3
"""Module to find the largest integer in a list
"""


def max_integer(list=[]):
    """This will find and return the largest integer in a list of integers
        the function returns None if the list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    a = 1
    while a < len(list):
        if list[a] > result:
            result = list[a]
        a += 1
    return result
