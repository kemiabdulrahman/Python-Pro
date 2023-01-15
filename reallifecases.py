from itertools import groupby
from operator import itemgetter

data = [{"name": "John", "age": 30, "gender": "male"},
        {"name": "Emily", "age": 25, "gender": "female"},
        {"name": "Michael", "age": 35, "gender": "male"},
        {"name": "Sarah", "age": 40, "gender": "female"}]

data = sorted(data, key=itemgetter('gender'))
grouped_data = {key: list(group) for key, group in groupby(data, itemgetter('gender'))}

print(grouped_data)

# 2 sorted
employees = {101: 'Bob', 102: 'Sue', 103: 'Mike', 104: 'Amy'}
evaluations = {101: 'Excellent', 102: 'Good', 103: 'Needs Improvement', 104: 'Outstanding'}

sorted_evaluations = sorted(evaluations.items(), key = lambda kv: kv[1])

print("Employees sorted by evaluation:")
for employee in sorted_evaluations:
    print(f"{employees[employee[0]]} - {employee[1]}")
# 3
products = {1: 'Apple', 2: 'Banana', 3: 'Cherries', 4: 'Donuts'}
prices = {1: '1.5', 2: '0.5', 3: '2', 4: '3'}

sorted_products = sorted(prices.items(), key = lambda kv: kv[1])

print("Products sorted by price:")
for product in sorted_products:
    print(f"{products[product[0]]} - {product[1]}$")



# 4



prices = [5, 10, 15, 20]
quantities = [2, 3, 4, 5]

costs = map(lambda x, y: x * y, prices, quantities)
print(list(costs))


# 5. password strength

def char_frequency(password):
    frequency = {}
    for char in password:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

password = input("Enter the password:")
frequency = char_frequency(password)
password_strength = 0

for char, count in frequency.items():
    password_strength += count

if password_strength >= 8:
    print("Strong password")
else:
    print("Weak password")



# 6
import os

def change_char(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    prefix = 'prefix_'
    file_name = prefix + file_name
    new_file_path = file_name + file_extension
    os.rename(file_path, new_file_path)
    return new_file_path

file_path = 'example.txt'
new_file_path = change_char(file_path)
print(f'File path changed to {new_file_path}')


