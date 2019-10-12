for letter in ['c', 'a', 't']:
    print(letter)
print(letter)  # last item iterated is what is assigned to the variable

animals = ['cat', 'dog', 'bird']
for index, value in enumerate(animals):
    print(index, value)

# 'break' out of a loop
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        break
    result += item          # augmented assignment: essentially 'result = result + item'
print(result)

# 'continue' to skip over an item
result = 0
for item in numbers:
    if item < 0:            # adds just the positive numbers
        continue
    result += item
print(result)

# wrong way to remove items from a list during iteration:
names = ['John', 'Paul', 'George', 'Ringo']
for name in names:
    if name not in ['John', 'Paul']:
        names.remove(name)
print(names)
# there are two correct ways to remove items from a list during iteration
# 1. collect the items that need to be removed into a list then iterate over that list
names = ['John', 'Paul', 'George', 'Ringo']
names_to_remove = []
for name in names:
    if name not in ['John', 'Paul']:
        names_to_remove.append(name)
for name in names_to_remove:
    names.remove(name)
print(names)
# 2. iterate over a copy of the list instead by 'slicing' using [:]
names = ['John', 'Paul', 'George', 'Ringo']
for name in names[:]:       # copy of names
    if name not in ['John', 'Paul']:
        names.remove(name)
print(names)

# else statements in 'for' loops
# this checks if numbers in a loop are positive:
items = [1, 2, 3, -4, 5]
positive = False
for num in items:
    if num < 0:
        break
    else:
        positive = True
print(positive)

# while loops
n = 3
while n > 0:
    print(n)
    n = n - 1
# or use a 'breal' statement to leave a loop
n = 3
while True:
    print(n)
    n = n - 1
    if n == 0:
        break

# EXERCISES

# 1
friends = ['Joshua', 'Jacob', 'Devin', 'Holly', 'Olivia']
length = 0
for name in friends:
    length += len(name)
avg_length = length / len(friends)
print(avg_length, 'letters')

# 2
man = False
for name in friends:
    if name == 'John':
        man = True
        break
    else:
        man = False
if not man:
    print('John not found!')
else:
    print('There is a John!')
