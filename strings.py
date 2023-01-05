#!/usr/bin/python3
""" 1. Program to calculate the length of a String """
"""
def string_length(string):
    count  = 0
    for char in string:
        count += 1
    return count
print(string_length("W3Resources"))
"""

""" 2. Program to count number of characters in a String """
"""
def char_count(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_count("W3Resources"))
"""



""" 3. Program to filter the positive numbers from a list """
"""
def filter_pn(num):
    return list(filter(lambda x : x > 0, num))
   
print(filter_pn([34, -78, 23, 56, -1, -2, 34]))
"""



""" 3. Program to get a string made of the first 2 and the last 2 characters from a given string"""
"""def string_both_ends(string):
    if len(string) < 2:
        return ''
    return string[0:2] + string[-2:]
print(string_both_ends('AbdulRahman MAFE'))
print(string_both_ends('MANLY'))
   """


""" 4. Program to get a string where all occurrences of its first char have been changed to $ except the first character itself"""
"""
def changed_char(string):
    char = string[0]
    string = string.replace(char, '$')
    string = char + string[1: ] 
    return string

print(changed_char('hehe '))
print(changed_char("resources"))
"""

"""
def change_num(string):
     num = string[1]
     '''keeping the num variable from going through replacement'''
     string = string.replace(num, '&')
     string = string[0] + num + string[2:]
     return string
print(change_num('W3Reso3urces'))
print(change_num('C12hexa1decimal'))
"""


""" 5. Program to get a single string from two given strings separated by a space and swap the first two characters of each string"""
"""
def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))
print(chars_mix_up('Temi', 'Kroos'))
"""




""" 6. Program to add ing at the end of a given string(length should be at least 3). if the given string already ends with ing
then add 'ly' instead. if the string length of the given string is less than 3, leave it unchanged.
"""

"""

def add_string(string):
    length = len(string)
    if length > 2:
        if string[-1:-4] == 'ing':
            string += 'ly'
        else:
            string += 'ing'
    return string
     

print(add_string("bit"))
print(add_string("rising"))
print(add_string("mi"))
"""




""" 7. Program to find the first appearance of the substring 'not' and 'poor' from the given string. if 'not' follows the 
'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting substring
"""
"""
def not_poor(string):
    snot = string.find("not")
    spoor = string.find("poor")

    if spoor > snot and snot > 0 and spoor > 0:
        string = string.replace(string[snot:(spoor+4)], 'good')
        return string
    else:
        return string
print(not_poor("The man is not that poor"))
print(not_poor("A man is poor if he has no change on him"))
"""
    




"""
 8. Program that takes a lists of words and return the longest word and the length of the longest one.
"""


"""
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append(len(n), n)
    word_len.sort()
    print(word_len)
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "JavaScript", "English"])
print(result[1])
print(result[0])
"""
    



""" 9. Program to remove nth index character from a non-empty index.
"""

def remove_char(string, n):
    prev = string[:n]
    last = string[n+1:]
    return prev + last
print(remove_char("Python Syntax", 4))
print(remove_char("Hello World", 7))
   

""" 10. Program to change a given string to a new string where the first and last chars have been exchanged
"""

def change_sring(string):
    return string[-1:] + string[1:-1] + string[:1]

print(change_sring("Hello World"))
    

""" 11. Program to remove the characters which have odd index values of a given string. """
def odd_values_string(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result = result + string[i]
    return result
print(odd_values_string('Abeokuta'))
print(odd_values_string('YOU'))






""" 12. Program to  count the occurrences of each word in a given sentence."""

def word_count(string):
    counts = dict()
    words = string.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] =  1
    return counts

print(word_count("Junior is the good boy there"))

 

""" 13. script that takes input from the user and displays that input back in upper and lower cases."""
user = input("Enter your favourite subject  ")
result = user.upper()
print(result)




""" 14. Program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)"""

user_input = input("Enter a comma separated sequence of colors to be sorted")
result = [word for word in user_input.split(",")]
print(",".join(sorted(list(set(result)))))



""" 15. Program to create the HTML string with tags around the word(s)"""
def tags_insertion(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
print(tags_insertion("li", "people"))
print(tags_insertion("b", "Python Tutorial"))






""" 16. Program to insert a string in the middle of a string"""
def middle_string_insertion(naive, main):
    return main[:2] + naive + main[2:]

print(middle_string_insertion("[[]]", 'Python'))
print(middle_string_insertion('<<>>', 'PHP'))
print(middle_string_insertion("{{}}", "HTML"))




""" 17. Program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)"""
def last_copies(string):
    if len(string) > 2:
        return string[-2:] * 4
    else:
        return string

print(last_copies('Python'))
print(last_copies('Hello'))


def insert_end(string):
    sub_string = string[-2:]
    return sub_string * 4




""" 18. Program to  get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string."""

def last_th_characters(string):
    if len(string) > 3:
        return string[:3]
    else:
        return string

print(last_copies('Python'))
print(last_copies('Hello'))


def first_three(str):
    return str[:3] if len(str) > 3 else str 


print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))




""" 19. Program to get the last part of a string before a specified character."""
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])



""" 20. Program to reverses a string if it's length is a multiple of 4"""

def reverse_string(str):
    for i in range(len(str)):
        if i % 4 == 0:
            return reversed(str) 
















