#!/usr/bin/python3
""" 1. Program to sum all items in a list"""
"""
def sum_all(sample):
    result = 0
    for num in sample:
        result += num
    return result
print(sum_all([1, 2, 89]))
"""

""" 2. Program to Multiply all items in a list"""
"""
def mul_all(sample):
    result = 1
    for num in sample:
        result *= num
    return result
print(mul_all([1, 2, 89]))
"""
""" 3. Get the largest number from a list"""
"""
def max_num_in_list(sample):
    maximum = sample[0]
    for num in sample:
        if num > maximum:
            maximum = num
    return maximum
print(max_num_in_list([1, 2, 89, -54, 12]))
"""


""" 4. Get the smallest number from a list"""

"""
def min_num_in_list(sample):
    minimum = sample[0]
    for num in sample:
        if num < minimum:
            minimum = num
    return minimum
print(min_num_in_list([1, 2, 190, -567, 12, 45]))
"""

""" 5. Program to count the number of strings where the string length is 2 or more and the first and last character 
are same from a given list of string
"""
"""
def match_words(words):
    counter = 0
    for word in words:
        if len(words) > 1 and word[0] == word[-1]:
            counter += 1
    return counter
print(match_words(['ABA', 'ABEOKUTA', 'OJA', 'ABBINTA']))

"""
""" 6. Program to get a list, sorted in increasing order by the last element in
each tuple from a given list of non-empty tuples.
"""
"""
def last(n):
    return n[-1]
def first(n):
    return n[0]

def sort_list_first(tuples):
    return (sorted(tuples, key = first))
def sort_list_last(tuples):
    return (sorted(tuples, key = last))
print(sort_list_first([(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)]))
print(sort_list_last([(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]))
"""


""" 7. Program to remove duplicates from a list
"""
"""
a = [10, 10, 20, 30, 90, 53, 34, 30, 20]
duplicate_items = set()
unique_items = []
for x in a:
    if x not in duplicate_items:
        unique_items.append(x)
        duplicate_items.add(x)
print(duplicate_items)
print(unique_items)
"""



""" 8. Program to check a list if empty or not
"""
"""
print("------A-----")
a = []
if not a:
    print("List is Empty")
print("---- B----")
b = [23, 1, 4]
if not b:
    print("List is empty")
else:
    print("Not an Empty list")
"""


""" 9. Program to Clone or Copy a list
"""
"""
previous_list = [10, 20, 30,40]
new_list = list(previous_list)
print(f"New List : {new_list}")
print(f"previous_list --> {previous_list}")
"""


""" 10. Program to find the list of words that are longer than n from a given list of words
"""

def long_words(n, string):
    word_len = []
    txt = string.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

print(long_words(3, "Hello man, A fox Entered into the forest just now."))



""" 11. Program that takes two lists and returns True if they have at least one common member
"""

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
            return result
print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))

""" 12. Program to print a specified list after removing the 0th, 4th and 5th elements.
"""
ages = [12, 13, 45, 67, 90]
colors = ["Red", "White", "Blue", "Green", "Brown"]

c_result = [color for (counter, color) in enumerate(colors) if counter not in (0, 4, 5)]
a_result = [age for (counter, age) in enumerate(ages) if age not in (1, 2, 3)]




""" 13. Program to to generate a 3*4*6 3D array whose each element is *
"""







""" 14. Program to print the numbers of a specified list after removing even numbers from it.
"""

def no_even_list(numbers_l):
    return [i for i in numbers_l if i % 2 != 0]

print(no_even_list([1, 2, 3, 4, 5, 6, 7]))
    

""" 15. Program to shuffle and print a specified list.
"""
from random import shuffle
fruits = ["Apple","Grape", "Banana", "Grape"]
shuffle(fruits)
print(fruits)




""" 16. Program to  generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
"""

def printValues():
    l = list()
    for i in range(1, 31):
        l.append(i ** 2)
    print(l[:5])
    print(l[-5:])
printValues()


""" 17. Program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
"""

def printValue():
    l = list()
    for i in range(1, 31):
        l.append(i ** 2)
    print(l[5:])
printValues()





""" 18. Program to generate all permutations of a list in Python.
"""
import itertools
print(list(itertools.permutations([1, 2, 3])))
print(list(itertools.permutations([5, 6, 2,1])))





""" 19. Program to get the difference between the two lists. 
"""
list1 = [1,3, 5, 7, 9]
list2 = [1, 2, 4, 6, 7, 8]
list_difference_1 = list(set(list1) - set(list2))
list_difference_2 = list(set(list2) - set(list1))
total_difference = list_difference_1 + list_difference_2
print(total_difference)







""" 20. Program to access the index of a list.
"""

nums = [5, 15, 35, 8, 98]
for counter, num in enumerate(nums):
    print(counter, num)
