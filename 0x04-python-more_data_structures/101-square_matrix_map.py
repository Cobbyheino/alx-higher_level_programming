#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row_1: list(map(lambda colon: colon**2, row_1)), matrix))
