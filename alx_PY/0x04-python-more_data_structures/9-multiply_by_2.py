#!/usr/bin/python3
"""
* Write a function that returns a new dictionary with all values multiplied by 2 
Algol:
    1. 
    2. 
    3.
    4.
    5.
    6.
"""

def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())
    for i in list_keys:
        new_dir[i] *= 2
    return (new_dir)

