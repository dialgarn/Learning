# empty strings evaluate to false while non-empty strings evaluate to true
# print(bool(''))
# print(bool('0'))


# if occurs when true and else is false
name = ('Paul')
if name:
    print('The name is {}'.format(name))
else:
    print('Name is missing')

# zero evaluates to false while other numbers have 'truthy' behavior
# print(bool(0))
# print(bool(4))


def hello():
    print('hi')


result = hello()
print(result)


a = None
b = None
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

if a is None:  # this is explicit
    print('A is not set!')

if not a:  # other things can evaluate to false and not necessarily 'None'
    print('A is not set!')

    # EXERCISES

# 1
age = 17
old = age >= 18

if old:
    print('You my friend are old!')
else:
    print('You are a youngster!')

# 2
name = 'devin'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
second_half = alphabet.find(name[0])

print(second_half)

if second_half > 12:
    print('Your name is in the second half of the alphabet!')
else:
    print('Your name in in the first half of the alphabet!')

# 3
names = ['Devin', 'Connor']
if names:
    print('Class has enrollments')
else:
    print('The class is empty')

# 4
car = None

if car is None:
    print('Taxi for you')
else:
    print('You have a car!')
