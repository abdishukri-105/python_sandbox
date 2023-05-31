# A List is a collection which is ordered and changeable. Allows duplicate members.


# create list
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'green','pears']

# get values
print(fruits[1])
print(len(fruits))
fruits.append('Mangoes')

fruits.remove('green')

# change values
fruits[0] = 'bluebarries'

# insert into position
fruits.insert(2, 'banana')

# remove with pop
fruits.pop(2)

fruits.reverse()

fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)