my_pets = ['dog', 'cat', 'bird']
print(my_pets[0])   # pulls out the first item

# negative indexing pulls out the last item
# a[-X] essentially means a[len(a)-X]
print(my_pets[-1])

# indexing also works on tuples and strings
print(('Fred', 23, 'Senior')[1])
print(('Fred')[0])

# Slicing - [start:end:stride]
print(my_pets[0:2])
print(my_pets[:2])  # defaults to start at 0
print(my_pets[0:-1])
print(my_pets[:-1])  # defaults to start at 0
# you don't need to provide start and end indices
# this is a good way to create a copy of a list
print(my_pets[:])
# Slices using strides
print(my_pets[0:3:2])
print(my_pets[::2])
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[::3])
print(numbers[::-1])    # negative strides go backwards; -1 reverses the sequence

# EXERCIES

# 1
name = 'Devin'
print(name[0])
print(name[-1])
print('{},'.format(name[0]), name[-1])
print('First character: {}; Last character: {}'.format(name[0], name[-1]))

# 2
filename = 'README.txt'
print(filename[-3:])

# 3


def is_palindrome(a):
    # determines if a supplied word is the same if the letters were reveresed
    if a == a[::-1]:
        return print(a, 'is INDEED a palindrome!')
    else:
        return print(a, 'is NOT a palindrome!')


is_palindrome('hello')
is_palindrome('mom')
