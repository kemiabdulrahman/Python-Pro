#!/usr/bin/python3
"""
* Write a function that prints a dictionary by ordered keys.
Algol:
    1. Define your function taking a dictionary variable as its parameter.
    2. initialize a variable to be equals to the list(not map) of the dictionary of the keys.
    3. use the sort inbuilt function to sort the variable in step 2
    4. loop through using a variable the variable in step 2
    5. print your result using the formatted string format having the variable used in looping : get method of the dictionary of the variable used in looping.
    

"""
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for i in list_ord:
        print("{} : {}".format(i, a_dictionary.get(i)))
