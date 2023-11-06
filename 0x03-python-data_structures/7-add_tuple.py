#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_1, b_1 = len(tuple_a), len(tuple_b)
    new_tuple = ((tuple_a[0] if a_1 >= 1 else 0) +
                 (tuple_b[0] if b_1 >= 1 else 0),
                 (tuple_a[1] if a_1 >= 2 else 0) +
                 (tuple_b[1] if b_1 >= 2 else 0))
    return new_tuple
