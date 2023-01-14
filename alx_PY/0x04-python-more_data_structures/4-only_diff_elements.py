#!/usr/bin/python3
"""
* Write a function that returns a set of all elements present in only one set.
Algol:
    1. define your function taking two sets as parameters.
    2. return the two sets having the pow symbol in between them.
"""
def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)
