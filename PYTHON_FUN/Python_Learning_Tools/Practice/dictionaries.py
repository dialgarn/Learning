info = {'first': 'Pete', 'last': 'Best'}
# other ways to create dictionaries
# info = dict([('first', 'Pete'),
#              ('last', 'Best')])
# or you can use the parameters
# info = dict(first='Pete', last='Best')

# you can insert values into a dictionary by using index operations
info['age'] = 20
info['occupation'] = 'Drummer'

# checking membership using 'in'
print('Band' in info)
print('age' in info)

# 'get' method
genre = info.get('Genre', 'Rock')

# 'setDefault' method
names = ['Ringo', 'Paul', 'John', 'Ringo']
count = {}
for name in names:
    count.setdefault(name, 0)
    count[name] += 1
print(count['Ringo'])
# without the 'setDefault' method, it requires more code
count = {}
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1
print(count['Ringo'])
# or use the 'collection.Counter' class
import collections
count = collections.Counter(names)
print(count)
print(count['Ringo'])
print(count['Fred'])

band1_names = ['John', 'Paul', 'George', 'Ringo']
band2_names = ['Paul']
names_to_bands = {}
for name in band1_names:
    names_to_bands.setdefault(name, []).append('Beatles')
for name in band2_names:
    names_to_bands.setdefault(name, []).append('Wings')
print(names_to_bands['Paul'])
# it can be more readable by using 'defaultDict'
from collections import defaultdict
names_to_bands = defaultdict(list)
for name in band1_names:
    names_to_bands[name].append('Beatles')
for name in band2_names:
    names_to_bands[name].append('Wings')
print(names_to_bands['Paul'])

# removing items from dictionaries
# deletes 'Ringo' from the dictionary
del names_to_bands['Ringo']

# dictionary iteration
# when iterating over a dictionary, by default it returns the key
data = {'Adam': 2, 'Zeek': 5, 'Fred': 3}
for name in data:
    print(name)
# to return the values, use the 'value' method
for value in data.values():
    print(value)
# to return both the keys and values, use the 'items' method
for key, value in data.items():
    print(key, value)

# by materializing a dictionary into a list, it returns the set of tuples (key, value)
    # the same thing that 'dict' accepts to create a dictionary
print(list(data.items()))

# dictionary item order is based on insertion order, but it can be sorted
for name in sorted(data.keys()):
    print(name)
# it can also be reversed
for name in sorted(data.keys(), reverse=True):
    print(name)

# you can have keys of mixed types, but it is not recommended; it is too confusing for readers
    # and python has a hard time sorting it
weird = {1: 'first', '1': 'another first'}
print(weird[1])
print(weird['1'])


# EXERCISES

# 1
info = {'first': 'Devin', 'last': 'Williams', 'age': 17}

# 2
phone = {}
phone['Screen Size'] = '6.1 inches'
phone['Storage'] = '128 gb'
phone['Brand'] = 'Apple'
print(phone)

# 3
paragraph = """Sunset is the time of day when our sky meets the outer space solar winds.
There are blue, pink, and purple swirls, spinning and twisting, like clouds of balloons
caught in a whirlwind. The sun moves slowly to hide behind the line of horizon, while the
moon races to take its place in prominence atop the night sky. People slow to a crawl, entranced,
fully forgetting the deeds that must still be done. There is a coolness, a calmness, when the
sun does set."""

para_count = collections.Counter(paragraph.split())
print(para_count)

# 4
# done - it is the same as #3

# 5
# don't understand

# 6
# don't understand
