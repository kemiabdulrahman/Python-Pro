"""
* map(function, iterable)
* 
"""

"""
1. map can listify the strings individually
"""
"""
l = ['sat', 'eat', 'mine']
result = list(map(list, l))
print(result)

"""


"""
2. Add two lists using map and lambda
"""
"""
CA = [12, 29, 23]
Exam = [69, 46, 56]
result = map(lambda x, y : x + y, CA, Exam)
print(list(result))
"""

"""
3. Double all numbers using map and lambda.
"""
"""

EXAM = [69, 46, 56, 45, 89, 123, 14]
result = map(lambda x : 2 * x, EXAM)
print(list(result))

"""


"""
4. Return double of n.
"""
"""
def multiple(x, y):
    return x * y

number = [12, 13, 14, 15, 16]
multiplier = [2, 3, 4, 5, 6]

result = map(multiple, number, multiplier)
print(list(result))
"""


# Python Dictionary keys() method


"""
1. Accessing the keys() function using the keys() function
"""
"""
dict = {"A": 'Geeks for Geeks', "B": 'Pyramid', "C": 'W3 School', "D": 'W3 Resources'}
print(dict.keys())
"""


"""
2. Python access dictionary by key.
"""
"""
dict = {"A": 'Geeks for Geeks', "B": 'Pyramid', "C": 'W3 School', "D": 'W3 Resources'}
j = 0
for i in dict:
    if j == 1:
        print("2nd key: " + i)
    j = j + 1
"""



"""
3. Accessing key using keys() indexing
"""
"""
dict = {"A": 'Geeks for Geeks', "B": 'Pyramid', "C": 'W3 School', "D": 'W3 Resources'}
print (list(dict.keys())[2])
"""




# Python Lambda.
"""
calc = lambda number: 'Even Number' if number % 2 == 0 else 'Odd Number'
print(calc(130))


filter_number = lambda s: "".join([ch for ch in s if not ch.isdigit()])
print(filter_number('Hello Jupyter 123'))
do_apostrophe = lambda str : '"' + str + '"'
print(do_apostrophe('Hello Bayyu'))

#find_sum = lambda n : sum([int(num) for num in str(n)])
#print(find_sum(901))


find_mul = lambda n: ([ num * num * num for num in n])
print(find_mul(123))

do_exclamation = lambda s: s + '!'
print(do_exclamation("Alas"))

comment = lambda str : '#' + str
print(comment("You "))

filter_letters = lambda str : ''.join([ch for ch in str if not ch.isalpha()])
filter_letters("Hello 123")

lambda_cube = lambda x: x ** 3
print(lambda_cube(12))




l = ["23", "12", "10", "13", "900"]
print("Sorted Numerically\n")

print("Filtered Positive Even Numbers\n")
print(list(filter(lambda x: not(int(x) % 2 == 0 and int(x) > 0), l)))



print("Operation on each item using lambda and map")
players = ["Salah", "Ronaldo", "Haaland"]
print(list(map(lambda x: x + " 10", players)))

"""

"""
# Python List, Dictionary Comprehension

odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1 ]
print(odd_square)

# Power of 3 from 1 to 5
power_of_3 = [x ** 3 for x in range(1, 6)]


# List of Prime Numbers and Non Prime Numbers. 
no_primes = []
primes = []

# List for lowering the character
print([x.lower() for x in ["A", "B", "C"]])


# list which extracts number.
str = "Phone Number: 08145854248"
Phone_Number = [x for x in str if x.isdigit()]
print(Phone_Number)



# List for Multiplication Table
a = 6
table = [[a, b, a * b] for b in range(1, 11)]
print("Multiplication Table 1 - 11")
for i in table:
    print(i)
"""


"""
Heap Queue in Python = Data Structure in Python
* heapify(iterable)
"""
# Creating a Simple Heap.
import heapq
li = [7, 8, 12, 90, 2, 1]
heapq.heapify(li)
print("The Created Heap : ", (list(li)))



Basketball_Team = {
        'Jordan' : 'Rockies',

        'Minnesota' : 'Badstaudi',
        'Seattle' : 'James',
        'Milwaukee' : 'Red Sox',
        'Jefferson' : 'Twins',
        'Harrison' : 'Brewers',
        'Allomp' : 'MarAllomp'
        }

# Using build.keys.
keys = Basketball_Team.keys()
print(keys)

# Using for loop
for players in Basketball_Team:
    print(players)

print('\n')
# Iterate through all values using values()
for location in Basketball_Team.values():
    print(location)
print('\n')
# Iterate through all key, and value pairs using items

for players, location in Basketball_Team.items():
    print(players ,'->', location)

print('\n')


# Access both key and value without using items()
for i in Basketball_Team:
    print(i, '->', Basketball_Team[i])



# Print items in key value pair
for i in Basketball_Team:
    print(



# Access both key and value without using items()
for i in Basketball_Team:
    print(i, '->', Basketball_Team[i])



