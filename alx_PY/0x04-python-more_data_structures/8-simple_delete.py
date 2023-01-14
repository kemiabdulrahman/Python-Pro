#!/usr/bin/python3
"""
* Write a function that deletes a key in a dictionary.
Algol:
    1. Define your function taking a variable representing the dictionary and a variable taking in the key to be an empty string.
    2. condition to check if the dictionary key is not empty using the get method
    3. delete the key.
    4. return the dictionary
"""
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)

