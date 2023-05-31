# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# create tuple

fruits = ('apple', 'orange', 'grapes')

# single value needs a trailing comma
fruits2 = ('apples',)

print(fruits2, type(fruits2))

# get a value 
print(fruits[1])

# cant change value it will show error since tuple cannot be changed
# fruits[0] = 'pears' 

# delete tuple
del  fruits2

print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a new set
fruit_set = {'apples', 'bananas', 'Mango'}

# check if in set
print('apples' in fruit_set)

# add to set 
fruit_set.add('grape')

# clear set 

fruit_set.clear()

# delete
del fruit_set

print(fruit_set)

