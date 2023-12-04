#!/usr/bin/python3
"""Define an inherited list class which is MyList."""


class MyList(list):
    """Implement sorted printin the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
