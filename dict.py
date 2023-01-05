capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)

capital_city["Japan"] = "Tokyo"

print("Updatcapital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ",capital_city)ed Dictionary: ",capital_city)



MLB_team = {
        ...     'Colorado' : 'Rockies',
        ...     'Boston'   : 'Red Sox',
        ...     'Minnesota': 'Twins',
        ...     'Milwaukee': 'Brewers',
        ...     'Seattle'  : 'Mariners'
        ... }

m = dict([
    ...     ('Colorado', 'Rockies'),
    ...     ('Boston', 'Red Sox'),
    ...     ('Minnesota', 'Twins'),
    ...     ('Milwaukee', 'Brewers'),
    ...     ('Seattle', 'Mariners')
    ... ])






>>> person = {}
>>> type(person)
<class 'dict'>

>>> person['fname'] = 'Joe'
>>> person['lname'] = 'Fonebone'
>>> person['age'] = 51
>>> person['spouse'] = 'Edna'
>>> person['children'] = ['Ralph', 'Betty', 'Joey']
>>> person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}







>>> person
{'fname': 'Joe', 'lname': 'Fonebone', 'age': 51, 'spouse': 'Edna',
        'children': ['Ralph', 'Betty', 'Joey'], 'pets': {'dog': 'Fido', 'cat': 'Sox'}}

>>> person['fname']
'Joe'
>>> person['age']
51
>>> person['children']
['Ralph', 'Betty', 'Joey']





>>> foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
>>> foo
{42: 'aaa', 2.78: 'bbb', True: 'ccc'}

>>> foo[42]
'aaa'
>>> foo[2.78]
'bbb'
>>> foo[True]
'ccc'






>>> MLB_team = {
        ...     'Colorado' : 'Rockies',
        ...     'Boston'   : 'Red Sox',
        ...     'Minnesota': 'Twins',
        ...     'Milwaukee': 'Brewers',
        ...     'Seattle'  : 'Mariners'
        ... }

>>> 'Milwaukee' in MLB_team
True
>>> 'Toronto' in MLB_team
False
>>> 'Toronto' not in MLB_team
True









