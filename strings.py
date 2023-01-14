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
- initialize the dict variable as a dictionary
- loop through the string
- initialize a variable key as the dictionary key
- make a condition to check if the variable looped is part of the key
- increament or decreament the dict of n 
- return the dict variable value.

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

# To count an elements in a list
def count_occ_num(my_list):
    counts = dict()
    for numbers in my_list:
        if numbers in counts:
            counts[numbers] += 1
        else:
            counts[numbers] += 1
            return counts
print(count_occ_num([1,1,1,2, 3, 4,5,4,5]))




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


"""
21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
"""
def to_upper(string):
    num_upper = 0
    for letter in string[:4]:
        if letter.upper() == letter:
            num_upper += 1
    if num_upper > 2:
        return string.upper()
    return string



"""
22.Write a Python program to sort a string lexicographically.
"""
def lexicographic_sort(str):
    return sorted(sorted(str), key =  str.upper)

print(lexicographic_sort("Hello World"))
print(lexicographic_sort('Doing good'))

"""
23. Write a Python program to remove a newline in Python.
"""
string = "Hello Unilorites\n"
print(string)
print(string.rstrip())

"""
24. Write a Python program to check whether a string starts with specified characters.
"""
string = "Long life and prosperity"
print(string.startswith("Lon"))

"""
25. Write a Python program to create a Caesar encryption.
Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
"""





26. Write a Python program to display formatted text (width=50) as output. Go to the editor
Click me to see the sample solution

27. Write a Python program to remove existing indentation from all of the lines in a given text. Go to the editor
Click me to see the sample solution

28. Write a Python program to add a prefix text to all of the lines in a string. Go to the editor
Click me to see the sample solution
"""

29. Write a Python program to set the indentation of the first line. Go to the editor
"""



"""
30. Write a Python program to print the following floating numbers upto 2 decimal places. Go to the editor
"""
x = 3.1236768
y = 12.90678
print("Original Number: ",x)
print("Formatted Number: "+"{:.2f}".format(x))
print("Original Number: ",y)
print("Formatted Number: "+"{:.2f}".format(y))


31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign. Go to the editor
Click me to see the sample solution

32. Write a Python program to print the following floating numbers with no decimal places. Go to the editor
Click me to see the sample solution

33. Write a Python program to print the following integers with zeros on the left of specified width. Go to the editor
Click me to see the sample solution

34. Write a Python program to print the following integers with '*' on the right of specified width. Go to the editor
Click me to see the sample solution

35. Write a Python program to display a number with a comma separator. Go to the editor
Click me to see the sample solution

36. Write a Python program to format a number with a percentage. Go to the editor
Click me to see the sample solution

37. Write a Python program to display a number in left, right and center aligned of width 10. Go to the editor
Click me to see the sample solution

38. Write a Python program to count occurrences of a substring in a string. Go to the editor
Click me to see the sample solution

39. Write a Python program to reverse a string. Go to the editor
Click me to see the sample solution

40. Write a Python program to reverse words in a string. Go to the editor
Click me to see the sample solution

41. Write a Python program to strip a set of characters from a string. Go to the editor
Click me to see the sample solution

42. Write a Python program to count repeated characters in a string. Go to the editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
Click me to see the sample solution

43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder. Go to the editor
Sample output:
The area of the rectangle is 1256.66cm2
The volume of the cylinder is 1254.725cm3
Click me to see the sample solution

44. Write a Python program to print the index of the character in a string. Go to the editor
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9
Click me to see the sample solution

45. Write a Python program to check whether a string contains all letters of the alphabet. Go to the editor
Click me to see the sample solution

46. Write a Python program to convert a given string into a list of words. Go to the editor
Sample Output:
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
Click me to see the sample solution

47. Write a Python program to lowercase first n characters in a string. Go to the editor
Click me to see the sample solution

48. Write a Python program to swap comma and dot in a string. Go to the editor
Sample string: "32.054,23"
Expected Output: "32,054.23"
Click me to see the sample solution

49. Write a Python program to count and display the vowels of a given text. Go to the editor
Click me to see the sample solution

50. Write a Python program to split a string on the last occurrence of the delimiter. Go to the editor
Click me to see the sample solution

51. Write a Python program to find the first non-repeating character in given string. Go to the editor
Click me to see the sample solution

52. Write a Python program to print all permutations with given repetition number of characters of a given string. Go to the editor
Click me to see the sample solution

53. Write a Python program to find the first repeated character in a given string. Go to the editor
Click me to see the sample solution

54. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest. Go to the editor
Click me to see the sample solution

55.Write a Python program to find the first repeated word in a given string. Go to the editor
Click me to see the sample solution

56. Write a Python program to find the second most repeated word in a given string. Go to the editor
Click me to see the sample solution

57.Write a Python program to remove spaces from a given string. Go to the editor
Click me to see the sample solution

58. Write a Python program to move spaces to the front of a given string. Go to the editor
Click me to see the sample solution

59. Write a Python program to find the maximum occurring character in a given string. Go to the editor
Click me to see the sample solution

60. Write a Python program to capitalize first and last letters of each word of a given string. Go to the editor
Click me to see the sample solution

61. Write a Python program to remove duplicate characters of a given string. Go to the editor
Click me to see the sample solution

62. Write a Python program to compute sum of digits of a given string. Go to the editor
Click me to see the sample solution

63. Write a Python program to remove leading zeros from an IP address. Go to the editor
Click me to see the sample solution

64. Write a Python program to find maximum length of consecutive 0's in a given binary string. Go to the editor
Click me to see the sample solution

65. Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print "No common characters". Go to the editor
Click me to see the sample solution

66. Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings. Go to the editor
Click me to see the sample solution

67. Write a Python program to remove all consecutive duplicates of a given string. Go to the editor
Click me to see the sample solution

68. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string. Go to the editor
Click me to see the sample solution

69. Write a Python program to find the longest common sub-string from two given strings. Go to the editor
Click me to see the sample solution

70. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings. Go to the editor
Click me to see the sample solution

71. Write a Python program to move all spaces to the front of a given string in single traversal. Go to the editor
Click me to see the sample solution

72. Write a Python code to remove all characters except a specified character in a given string. Go to the editor
Original string
Python Exercises
Remove all characters except P in the said string:
P
Original string
google
Remove all characters except g in the said string:
gg
Original string
exercises
Remove all characters except e in the said string:
eee
Click me to see the sample solution

73. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string. Go to the editor
Click me to see the sample solution

74. Write a Python program to find the minimum window in a given string which will contain all the characters of another given string. Go to the editor
Example 1
Input : str1 = " PRWSOERIUSFK "
str2 = " OSU "
Output: Minimum window is "OERIUS"
Click me to see the sample solution

75. Write a Python program to find smallest window that contains all characters of a given string. Go to the editor
Click me to see the sample solution

76. Write a Python program to count number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters. Go to the editor
Click me to see the sample solution

77. Write a Python program to count number of non-empty substrings of a given string. Go to the editor
Click me to see the sample solution

78. Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet. Go to the editor
Click me to see the sample solution

79. Write a Python program to find smallest and largest word in a given string. Go to the editor
Click me to see the sample solution

80. Write a Python program to count number of substrings with same first and last characters of a given string. Go to the editor
Click me to see the sample solution

81. Write a Python program to find the index of a given string at which a given substring starts. If the substring is not found in the given string return 'Not found'. Go to the editor
Click me to see the sample solution

82. Write a Python program to wrap a given string into a paragraph of given width. Go to the editor
Sample Output:
Input a string: The quick brown fox.
Input the width of the paragraph: 10
Result:
The quick
brown fox.
Click me to see the sample solution

83. Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer. Go to the editor
Sample Output:
Input an integer: 25
Decimal Octal Hexadecimal (capitalized), Binary
25 31 19 11001
Click me to see the sample solution

84. Write a Python program to swap cases of a given string. Go to the editor
Sample Output:
pYTHON eXERCISES
jAVA
nUMpY
Click me to see the sample solution

85. Write a Python program to convert a given Bytearray to Hexadecimal string. Go to the editor
Sample Output:
Original Bytearray :
[111, 12, 45, 67, 109]
Hexadecimal string:
6f0c2d436d
Click me to see the sample solution

86. Write a Python program to delete all occurrences of a specified character in a given string. Go to the editor
Sample Output:
Original string:
Delete all occurrences of a specified character in a given string
Modified string:
Delete ll occurrences of specified chrcter in given string
Click me to see the sample solution

87. Write a Python program find the common values that appear in two given strings. Go to the editor
Sample Output:
Original strings:
Python3
Python2.7
Intersection of two said String:
Python
Click me to see the sample solution

88. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length. Go to the editor
Sample Output:
Input the string: W3resource
['Valid string.']
Click me to see the sample solution

89. Write a Python program to remove unwanted characters from a given string. Go to the editor
Sample Output:
Original String : Pyth*^on Exercis^es
After removing unwanted characters:
Python Exercises
Original String : A%^!B#*CD
After removing unwanted characters:
ABCD
Click me to see the sample solution

90. Write a Python program to remove duplicate words from a given string. Go to the editor
Sample Output:
Original String:
Python Exercises Practice Solution Exercises
After removing duplicate words from the said string:
Python Exercises Practice Solution
Click me to see the sample solution

91. Write a Python program to convert a given heterogeneous list of scalars into a string. Go to the editor
Sample Output:
Original list:
['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
Convert the heterogeneous list of scalars into a string:
Red,100,-50,green,w,3,r,12.12,False
Click me to see the sample solution

92. Write a Python program to find the string similarity between two given strings. Go to the editor
Sample Output:
Original string:
Python Exercises
Python Exercises
Similarity between two said strings:
1.0
Original string:
Python Exercises
Python Exercise
Similarity between two said strings:
0.967741935483871
Original string:
Python Exercises
Python Ex.
Similarity between two said strings:
0.6923076923076923
Original string:
Python Exercises
Python
Similarity between two said strings:
0.5454545454545454
Original string:
Java Exercises
Python
Similarity between two said strings:
0.0
Click me to see the sample solution

93. Write a Python program to extract numbers from a given string. Go to the editor
Sample Output:
Original string: red 12 black 45 green
Extract numbers from the said string: [12, 45]
Click me to see the sample solution

94. Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components. Go to the editor
Sample Output:
(255, 165, 1)
(255, 255, 255)
(0, 0, 0)
(255, 0, 0)
(0, 0, 128)
(192, 192, 192)
Click me to see the sample solution

95. Write a Python program to convert the values of RGB components to a hexadecimal color code. Go to the editor
Sample Output:
FFA501
FFFFFF
000000
000080
C0C0C0
Click me to see the sample solution

96. Write a Python program to convert a given string to camelcase. Go to the editor
Sample Output:
javascript
fooBar
fooBar
foo.Bar
fooBar
foobar
fooBar
Click me to see the sample solution

97. Write a Python program to convert a given string to snake case. Go to the editor
Sample Output:
java_script
foo_bar
foo_bar
foo.bar
foo_bar
foo_bar
foo_bar
Click me to see the sample solution

98. Write a Python program to decapitalize the first letter of a given string. Go to the editor
Sample Output:
java Script
python
Click me to see the sample solution

99. Write a Python program to split a given multiline string into a list of lines. Go to the editor
Sample Output:
Original string: This
is a
multiline
string.
Split the said multiline string into a list of lines:
['This', 'is a', 'multiline', 'string.', '']
Click me to see the sample solution

100. Write a Python program to check whether any word in a given sting contains duplicate characrters or not. Return True or False. Go to the editor
Sample Output:
Original text:
Filter out the factorials of the said list.
Check whether any word in the said sting contains duplicate characrters or not!
False
Original text:
Python Exercise.
Check whether any word in the said sting contains duplicate characrters or not!
False
Original text:
The wait is over.
Check whether any word in the said sting contains duplicate characrters or not!
True
Click me to see the sample solution

101. Write a Python program to add two strings as they are numbers (Positive integer values). Return a message if the numbers are string. Go to the editor
Sample Output:
42
Error in input!
Error in input!
Click me to see the sample solution

102. Write a Python program to remove punctuations from a given string. Go to the editor
Sample Output:
Original text:
String! With. Punctuation?
After removing Punctuations from the said string:
String With Punctuation
Click me to see the sample solution

103. Write a Python program to replace each character of a word of length five and more with hash character (#). Go to the editor
Sample Output:
Original string: Count the lowercase letters in the said list of words:
Replace words (length five or more) with hash characters in the said string:
##### the ######### ####### in the said list of ######
Original string: Python - Remove punctuations from a string:
Replace words (length five or more) with hash characters in the said string:
###### - ###### ############ from a #######
Click me to see the sample solution

104. Write a Python program that capitalizes the first letter and lowercases the remaining letters of a given string. Go to the editor
Sample Data:
("Red Green WHITE") -> "Red Green White"
("w3resource") -> "W3resource"
("dow jones industrial average") -> "Dow Jones Industrial Average"
Click me to see the sample solution

105. Write a Python program to extract and display the name from a given email address. Go to the editor
Sample Data:
("john@example.com") -> ("john")
("john.smith@example.com") -> ("johnsmith")
("fully-qualified-domain@example.com") -> ("fullyqualifieddomain")
Click me to see the sample solution

106. Write a Python program to remove repeated consecutive characters and replace with the single letters and print new updated string. Go to the editor
Sample Data:
("Red Green White") -> "Red Gren White"
("aabbbcdeffff") -> "abcdef"
("Yellowwooddoor") -> "Yelowodor"
Click me to see the sample solution

107. Write a Python program to that takes two strings. Count the number of times each string contains the same three letters at the same index. Go to the editor
Sample Data:
("Red RedGreen") -> 1
("Red White Red White) -> 7
("Red White White Red") -> 0
Click me to see the sample solution

108. Write a Python program to that takes a string and returns # on both sides each element, which are not vowels. Go to the editor
Sample Data:
("Green" -> "-G--r-ee-n-"
("White") -> "-W--h-i-t-e"
("aeiou") -> "aeiou"
Click me to see the sample solution

109. Write a Python program that counts the number of leap years within the range of years. The range of years should be accepted as a string. Go to the editor
Sample Data:
("1981-1991") -> 2
("2000-2020") -> 6
Click me to see the sample solution

110. Write a Python program to insert space before every capital letter appears in a given word. Go to the editor
Sample Data:
("PythonExercises") -> "Python Exercises"
("Python") -> "Python"
("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"
Click me to see the sample solution

111. Write a Python program that takes a string and replaces all the characters with their respective numbers. Go to the editor
Sample Data:
("Python") -> "16 25 20 8 15 14"
("Java") -> "10 1 22 1"
("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"
Click me to see the sample solution

112. Write a Python program to calculate the sum of two numbers given as strings. Return the result in the same string representation. Go to the editor
Sample Data:
( "234242342341", "2432342342") -> "236674684683"
( "", "2432342342") -> False ( "1000", "0") -> "1000"
( "1000", "10") -> "1010"
Click me to see the sample solution

113. Write a Python program that returns a string sorted alphabetically by the first character of a given string of words. Go to the editor
Sample Data:
("Red Green Black White Pink") -> "Black Green Pink Red White"
("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")
Click me to see the sample solution












