#!/usr/bin/python3
"""
* Write a function that returns a list with all values multiplied by a number without using any loops.
Algol:
    1. return a list having map, lambda, and what we are to work upon(my_list)
"""
def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda x: x * number), my_list)))
