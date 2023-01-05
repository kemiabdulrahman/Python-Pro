#!/usr/bin/python3
""" 1. Program to calculate the length of a String """
def string_length(string):
    count = 0
    for i in string:
        count += 1
    return count


print(string_length("Hello World"))


""" 2. Program to count number of characters in a String """

def char_count(string):
    count = 0
    for i in string:
        if (i == ' ') or (i == ','):
            count += 0
        else:
            count += 1
    return count
print(char_count("W3 Resources 123"))


""" 3. Program to filter the positive numbers from a list """
def filter_positive_num(listA):
    pass

    



""" 3. Program to get a string made of the first 2 and the last 2 characters from a given string"""
def string_manip(string):
    first = string[:2]
    last = string[-2:]
    return first + last
print(string_manip("Hello World"))





""" 4. Program to get a string where all occurrences of its first char have been changed to $ except the first character itself"""

def changed_char(string):
   pass 




""" 5. Program to get a single string from two given strings separated by a space and swap the first two characters of each string"""
def swap_strings(listA):
    for i in listA:
        str1 = i[0]
        str2 = i[1]
        str1 = str1[0:2] + str2[-1:]
        str2  = str2[:2] + str1[-2:]
        return str1, str2

print(swap_strings(["john", "Bryan"]))




""" 6. Program to add ing at the end of a given string(length should be at least 3). if the given string already ends with ing
then add 'ly' instead. if the string length of the given string is less than 3, leave it unchanged.
"""







""" 7. Program to find the first appearance of the substring 'not' and 'poor' from the given string. if 'not' follows the 
'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting substring
"""







"""
 8. Program that takes a lists of words and return the longest word and the length of the longest one.
"""







""" 9. Program to remove nth index character from a non-empty index.
"""




""" 10. Program to change a given string to a new string where the first and last chars have been exchanged
"""





""" 11. Program to remove the characters which have odd index values of a given string. """







""" 12. Program to  count the occurrences of each word in a given sentence."""

 

""" 13. script that takes input from the user and displays that input back in upper and lower cases."""





""" 14. Program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)"""





""" 15. Program to create the HTML string with tags around the word(s)"""





""" 16. Program to insert a string in the middle of a string"""




""" 17. Program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)"""




""" 18. Program to  get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string."""






""" 19. Program to get the last part of a string before a specified character."""




""" 20. Program to reverses a string if it's length is a multiple of 4"""


















