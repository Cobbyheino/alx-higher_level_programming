#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    rep = 0
    digit = 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for r in reversed(roman_string):
        digit = data[r]
        rep += digit if rep < digit * 5 else -digit
    return rep
