#!/usr/bin/python3
"""
* Write a function that replaces or adds key/value in a dictionary.
Algol:
    1. Define your function taking a dictionary variable, the value variable, and the variable representing the key as its three parameter.
    2. make your step 1 dictionary variable of the key to be equals to the value variable.
    3. return your dictionary variable.
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
