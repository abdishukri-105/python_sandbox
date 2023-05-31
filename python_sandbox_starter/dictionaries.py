# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# create dictionary
person = { 
    'first_name': 'John',
    'last_name': 'doe',
    'age': 36
}


# get a value 

# print(person['first_name'])
# print(person.get('last_name')) 

# add key/value
person['phone'] = '555 6666 7737'

# copy dictionary

person2 = person.copy()
person2['city'] = "Nairobi"



# remove item
del(person['age'])
person.pop('phone')
person.clear()

# print(person.keys())
# print(person.items())

print(len(person2))



# list dictionaries

people = [
    {'name': 'martha', 'age': 30},
    {'name': 'shukri', 'age': 24},
    {'name': 'sumeya', 'age': 22}
]

print(people[1]['name'])