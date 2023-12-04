#!/usr/bin/python3
"""Defines an inherited class-check function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited  of a class.

    Args:
        obj (any): The object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
