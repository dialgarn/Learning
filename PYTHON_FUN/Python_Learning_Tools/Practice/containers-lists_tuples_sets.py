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
print('\n')


# TUPLES - are immutable
row = ('George', 'Guitar')
print(row)
# can use the function or the literal syntax to create empty tuples
empty = tuple()
empty2 = ()
# different ways to create tuples with a single item
one = tuple([1])
one_2 = (1,)
one_3 = 1,
# you need the comma to create a tuple
# just use the tuple function - its easier and you know it is going to be a tuple
d = (3)
print(d, type(d))
e = (3,)
print(e, type(e))

# more ways to create tuples; what I said before might not be the best way haha
# last way is the more pythonic way - uses parantheses which makes it easy to see that its a tuple
p = tuple(['Steph', 'Curry', 'Guard'])
q = 'Steph', 'Curry', 'Guard'
r = ('Steph', 'Curry', 'Guard')
print('\n')


# SETS; removes and do not contain duplicates
digits = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits_set = set(digits)    # removes the extra 1
print(digits_set)
digits_set2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  # literal syntax uses {}
# membership checking
# if something has the __contains__ method, 'in' can be used to check membership
print(9 in digits_set)
print(42 in digits_set)

# set operations: difference, intersection, union, Xor
odd = {1, 3, 5, 7, 9}
# difference; removes items in a set from another
even = digits_set - odd
print(even)
# intersection; has to be in both sets
prime = {2, 3, 5, 7}
prime_even = prime & even
print(prime_even)
# union; puts two sets together and removes duplicates
numbers = odd | even
print(numbers)
# Xor; things that are one in one set or the other, not both
first_five = {0, 1, 2, 3, 4}
two_to_six = {2, 3, 4, 5, 6}
in_one = first_five ^ two_to_six
print(in_one)
print('\n')


# EXERCISES

# 1
friends = []
print(id(friends))
friends.append('Josh')
print(id(friends))
friends.append('Jacob')
print(id(friends))
friends.append('Grace')
friends.append('Olivia')
print(friends)
friends.sort()
print(friends)
print(friends[0])
print(friends[3])
print('\n')

# 2
me = ('Devin', 'Williams', 17)
people = []
people.append(me)
friend1 = ('Josh', 'Aina', 18)
friend2 = ('Jacob', 'Aina', 16)
friend3 = ('Grace', 'Evans', 17)
friend4 = ('Olivia', 'Boyd', 16)
people.append(friend1)
people.append(friend2)
people.append(friend3)
people.append(friend4)
print(people)
people.sort()
print(people)
print('\n')

# 3
print(friends)
top10_guys = ['Noah', 'Liam', 'Mason', 'Jacob', 'William',
              'Ethan', 'James', 'Alexander', 'Michael', 'Benjamin']
top10_girls = ['Emma', 'Olivia', 'Sophia', 'Ava', 'Isabella',
               'Mia', 'Abigail', 'Emily', 'Charlotte', 'Harper']

for name in friends:
    if name in top10_girls:
        print('{},'.format(name), 'In top 10 girls!')
    elif name in top10_guys:
        print('{},'.format(name), 'In top 10 guys!')
    else:
        print('{},'.format(name), 'You\'re original!')
print('\n')

# 4
shakespeare_text = """HAMLET.
Speak the speech, I pray you, as I pronounced it to you,
trippingly on the tongue. But if you mouth it, as many of
your players do, I had as lief the town-crier spoke my lines.
Nor do not saw the air too much with your hand, thus, but use all gently;
for in the very torrent, tempest, and, as I may say, whirlwind of passion,
you must acquire and beget a temperance that may give it smoothness. O, it
offends me to the soul to hear a robustious periwig-pated fellow tear a passion
to tatters, to very rags, to split the ears of the groundlings, who, for the most part,
are capable of nothing but inexplicable dumb shows and noise. I would have such a
fellow whipped for o’erdoing Termagant. It out-Herods Herod. Pray you avoid it."""
emerson_text = """In the elder English dramatists, and mainly in
 the plays of Beaumont and Fletcher, there is a constant recognition
  of gentility, as if a noble behavior were as easily marked in the
  society of their age, as color is in our American population. When
  any Rodrigo, Pedro, or Valerio enters, though he be a stranger,
  the duke or governor exclaims, This is a gentleman,—and proffers civilities
  without end; but all the rest are slag and refuse. In harmony with this delight
  in personal advantages, there is in their plays a certain heroic cast of
  character and dialogue,—as in Bonduca, Sophocles, the Mad Lover, the Double
  Marriage,—wherein the speaker is so earnest and cordial, and on such
  deep grounds of character, that the dialogue, on the slightest additional
  incident in the plot, rises naturally into poetry. Among many texts,
  take the following. The Roman Martius has conquered Athens—all but the
  invincible spirits of Sophocles, the duke of Athens, and Dorigen, his wife.
  The beauty of the latter inflames Martius, and he seeks to save her husband;
  but Sophocles will not ask his life, although assured, that a word will
  save him, and the execution of both proceeds."""


ssplit = shakespeare_text.split()
esplit = emerson_text.split()

ssplit_set = set(ssplit)
esplit_set = set(esplit)

both_authors = ssplit_set & esplit_set
print('both_authors: {}'.format(both_authors), '\n')

shakespeare = ssplit_set - esplit_set
print('shakespeare only: {}'.format(shakespeare), '\n')
emerson = esplit_set - ssplit_set
print('emerson only: {}'.format(emerson), '\n')

# 5
tuple_attributes = dir(tuple)
list_attributes = dir(list)
tattributes = set(tuple_attributes)
lattributes = set(list_attributes)
print('\'list\' only attributes:', lattributes - tattributes)
