#!/usr/bin/python3
"""
* Write a function that replaces all occurrences of an element by another in a new list.
Algol:
    - define your function taking the following parameters: list involved, the value to replace, replacement value.
    - initialize the new list to be returned to be equals to  a mapped list having its lambda to replace if the value searched is seen else it should return the initial list of values.

"""
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
