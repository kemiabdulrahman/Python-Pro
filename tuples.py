#!/usr/bin/python3

""" 1. Program to create a tuple.
NOTE: WHEN testing, add a case study from your previous knowledge
"""


t = ()
print(t)
tuplex = tuple()
print(tuplex)




""" 2. Python program to create a tuple with different data types"""

tuplex = tuple("Hello World", 12, 13.4, [1, 2, 3], {"name": "Bolanle"})
print(tuplex)


 

""" 3. Python program to create a tuple with numbers and print one item"""
tuplex = 5, 10, 15, 20, 25
print(tuplex)
tuplex = 5,
print(tuplex)



""" 4. Program to unpack a tuple in several variables."""
tuplex = "Bredan Rodgers", 40, "Leicester City"
print(tuplex)
name, age, club = tuplex
print(name)
tuplex = 12, 34, 56
a, b, c = tuplex
print(a + b + c)





""" 5. Program to add an item in a tuple."""
tuplex = (4, 3, 2, 6, 7, 8, 3)
print(tuplex)
tuplex = tuplex + (9,)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
#converting the tuple into list
listx = list(tuplex)
#Use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)




""" 6. Program to convert a tuple to a string."""
string = ""
tuplex = ('a', 'n', 'd', 'r', 'e', 'w')
result = string.join(tuplex)
print(result)






""" 7. Python program to get the 4th element and 4th element from last of a tuple"""
tuplex = ("w" , "3", "r", "e", "s", "o", "u", "r", "c", "e", "s")
print(tuplex)
result = (tuplex[3])
print(result)
result_B = (tuplex[-4])
print(result_B)







""" 8. Python program to create the colon of a tuple."""
from copy import deepcopy
tuplex = (10.5, 23, [], 45, "Hello World")
t_colon = deepcopy(tuplex)
t_colon[2].append(67.89)
print(tuplex)
print(t_colon)





""" 9. Program to find the repeated items of a tuple.to find the repeated items of a tuple."""
tuplex = (1, 2, 1, 2, 3, 3, 3, 5, 6, 7, 4, 5, 6 ,4,4)
count = tuplex.count(3)
print(count)



""" 10. Program to check whether an element exists within a tuple"""
color = ("green", "brown", "pink", "green")
print("green" in color)
print(3 in color)














11. Write a Python program to convert a list to a tuple. Go to the editor

Click me to see the sample solution

12. Write a Python program to remove an item from a tuple. Go to the editor

Click me to see the sample solution

13. Write a Python program to slice a tuple. Go to the editor

Click me to see the sample solution

14. Write a Python program to find the index of an item of a tuple. Go to the editor

Click me to see the sample solution

15. Write a Python program to find the length of a tuple. Go to the editor

Click me to see the sample solution

16. Write a Python program to convert a tuple to a dictionary. Go to the editor

Click me to see the sample solution

17. Write a Python program to unzip a list of tuples into individual lists. Go to the editor

Click me to see the sample solution

18. Write a Python program to reverse a tuple. Go to the editor

Click me to see the sample solution

19. Write a Python program to convert a list of tuples into a dictionary. Go to the editor

Click me to see the sample solution

20. Write a Python program to print a tuple with string formatting. Go to the editor
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)

Click me to see the sample solution

21. Write a Python program to replace last value of tuples in a list. Go to the editor
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

Click me to see the sample solution

22. Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

Click me to see the sample solution

23. Write a Python program to sort a tuple by its float element. Go to the editor
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
Click me to see the sample solution

24. Write a Python program to count the elements in a list until an element is a tuple. Go to the editor
Click me to see the sample solution

25. Write a Python program convert a given string list to a tuple. Go to the editor
Original string: python 3.0
<class 'str'>
Convert the said string to a tuple:
('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
<class 'tuple'>
Click me to see the sample solution

26. Write a Python program calculate the product, multiplying all the numbers of a given tuple. Go to the editor
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648
Click me to see the sample solution

27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples. Go to the editor
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
[25.5, -18.0, 3.75]
Click me to see the sample solution

28. Write a Python program to convert a tuple of string values to a tuple of integer values. Go to the editor
Original tuple values:
(('333', '33'), ('1416', '55'))
New tuple values:
((333, 33), (1416, 55))
Click me to see the sample solution

29. Write a Python program to convert a given tuple of positive integers into an integer. Go to the editor
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570
Click me to see the sample solution

30. Write a Python program to check if a specified element presents in a tuple of tuples. Go to the editor
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White presenet in said tuple of tuples!
True
Check if White presenet in said tuple of tuples!
True
Check if Olive presenet in said tuple of tuples!
False
Click me to see the sample solution

31. Write a Python program to compute element-wise sum of given tuples. Go to the editor
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)
Click me to see the sample solution

32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples. Go to the editor
Original list of tuples:
[(1, 2), (2, 3), (3, 4)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[3, 5, 7]
Original list of tuples:
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[9, -1, 7, 8]
Click me to see the sample solution

33. Write a Python program to convert a given list of tuples to a list of lists. Go to the editor
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
Click me to see the sample solution


