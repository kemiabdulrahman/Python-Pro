#!/usr/bin/python3
"""
* Write a function that returns a set of common elements in two sets not having ().
Algol:
    1. define your function taking in two sets(data structure) of list.
    2. return the first set and the second set using an and i.e (&) operator in between them.
"""
def common_elements(set_1, set_2):
    return (set_1 & set_2)
