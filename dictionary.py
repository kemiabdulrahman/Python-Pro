"""
1. sort a dictionary by value
"""
import operator
d = {1:2, 3:4, 4:3, 2:1, 0:0}
print("original dictionary : " , d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print("Ascending Order by value : ", sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print("Descending order by value : ", sorted_d)


"""
2. Add a key to a dictionary.
"""

d = {1:2, 3:4, 4:3, 2:1, 0:0}
print(d)
d.update({8:30})
print(d)



"""
3. Concatenate following dictionaries to create a new one.
"""


d1 = {1:2, 3:4, 4:3, 2:1, 0:0}
d2 = {1:2, 3:4, 4:3, 2:1, 0:0}
d3 = {1:22, 33:41, 4:3, 2:1, 0:0}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)

"""
4. Check whether a given key already exists in a dictionary.
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print("Key is present in the dictionary")
    else:
        print("Not Present")

"""
5. Iterate over dictionary using for loop
"""
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for dict_key, dict_value in d.items():
    print(dict_key, "-->", dict_value)

"""
6.  script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
"""

"""
7. script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
"""
user_input = int(input("Input a number"))
d = dict()
for x in range(1, user_input+1):
    d[x] = x * x
print(d)

"""
8. script to merge two Python dictionaries.
"""

d1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d2 = {7: 10, 8: 20, 9: 30, 14: 40, 25: 50, 56: 60}
d = d1.copy()
d.update(d2)
print(d)


"""
9.  Program to iterate over dictionaries using for loops.
"""
d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
         print(color_key, 'corresponds to ', d[color_key]) 



"""
10.  Program to sum all the items in a dictionary
"""
dict = {"rice":100, "beans": 45, "yam": 243}
print(sum(dict.values()))

dict = {"rice":100, "beans": 45, "yam": 243}
result = 0
for key in dict:
    result = result + dict[key]


"""
11. Program to multiply all the items in a dictionary.
"""

dict = {"rice":100, "beans": 45, "yam": 243}
result = 1
for key in dict:
    result = result * dict[key]
print(result)


