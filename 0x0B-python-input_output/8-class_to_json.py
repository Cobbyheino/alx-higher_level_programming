#!/usr/bin/python3
"""Defyn a Python class to JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation ov a simple data structure."""
    return obj.__dict__
