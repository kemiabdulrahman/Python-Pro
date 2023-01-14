#!/usr/bin/python3
"""
* Write a function that computes the square value of all integers of a matrix using map
Algol:
    1.
    2.
    3.
    4.
    5.
    6.
"""
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
