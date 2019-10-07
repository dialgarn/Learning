# can invoke the list class or use brackets to create lists
names = list()
other_names = []
other_other_names = ['Fred', 'Charles']
# separates the characters into their own entities
print(list('Matt'))

# lists also have methods
# append method
names.append('Matt')
names.append('Paul')
print(names)

# lists are zero-based indexed
print(names[1])
print(names[0])

# insert method; inserts an item at the specific index and pushes everything to the right
names.insert(1, 'George')
print(names)
# replace method; replaces item at given index
names[1] = 'Fred'
print(names)

# removing objects from a list; can either input the item or use the index
names.append('John')
names.append('Riley')
print(names)

names.remove('Paul')
print(names)
del names[1]
print(names)

# sorting lists
# sort method does not create a new list
# rather it updates the old list
names.sort()
print(names)

# use the sorted function to make a copy of the old list if it is important
old = [5, 3, -2, 1]
nums_sorted = sorted(old)
print(nums_sorted)
print(old)
# sorting this way will return an error as the items are of diff types
things = [2, 'abc', 'Zebra', '1', -5]
# things.sort()
# print(things)

# to fix - sort everything as if it were a string
things.sort(key=str)
print(things)

# other fun things with lists
# range function
nums = range(5)
print(nums)
print(list(nums))
even = range(0, 11, 2)
print(list(even))
odd = range(1, 12, 2)
print(list(odd))

a = range(0, 5)
b = range(5, 10)
both = list(a) + list(b)
print(len(both))            # 10 - 0
print(both)
