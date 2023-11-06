#!/usr/bin/python3
def no_c(my_string):
    rev_c = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            rev_c += elements
    return rev_c
