#!/usr/bin/python3
"""
* Write a function that returns a key with the biggest integer value. 
Algol:
    1. condition to check if it is not a dictionary.
    2. if it is, return the maximum using the dictionary.get method
"""
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return (max(a_dictionary, key=a_dictionary.get))
