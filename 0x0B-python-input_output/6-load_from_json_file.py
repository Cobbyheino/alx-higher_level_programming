#!/usr/bin/python3
"""Defynes a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python obj from a JSON file."""
    with open(filename) as f:
        return json.load(f)
