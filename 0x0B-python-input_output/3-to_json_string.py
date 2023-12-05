#!/usr/bin/python3
"""Defyns a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation ov a string object."""
    return json.dumps(my_obj)
