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









""" 11. Program to
"""




""" 12. Python program to """



""" 13. Python program to """




""" 14. Program to """







""" 15. Program to """










""" 16. Program to """





""" 17. Python program to """




""" 18. Python program to """





""" 19. Program to """







""" 20. Program to """








 
