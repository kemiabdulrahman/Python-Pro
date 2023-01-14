#!/usr/bin/python3
"""
* Write a function that adds all unique integers in a list (only once for each integer).
Algol:
    1 define your function taking in the list as a parameter.
    2 initialize a variable equal to turn your list into a set.
    3 initialize a variable to take the sum of the list.
    4 loop through the list of the variable name in step 2.
    5 add loop variable in step 4 to the variable name in step 3.
    6 return the variable in step 3
"""
def uniq_add(my_list=[]):
    unique_list = set(my_list)

    num = 0
    for i in unique_list:
        num += i
    return (num)
