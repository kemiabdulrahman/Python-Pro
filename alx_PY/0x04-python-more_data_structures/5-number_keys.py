#!/usr/bin/python3
"""
* Write a function that returns the number of keys in a dictionary.
Algol:
    1. Define your variable taking a dictionary as its parameter 
    2. initialize a variable to take the number of the keys present in the dictionary as zero.
    3. initialize a variable to help in listing the keys present to be equals to list(mapped but not using map) of the parameter dictionary of the keys
    4. loop through the variable in step 3 .
    5. increament your variable in step 2 by 1.
    6. return the variable in step 2.

"""
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())
    for i in list_keys:
        num += 1
    return (num)

