def add_2(num):
    'return 2 more than num'
    result = num + 2
    return result


print(add_2(5))

# local, global, and built-in scopes
x = 2  # Global


def scope_demo():
    y = 4  # Local to scope_demo
    print('Local: {}'.format(y))
    print('Global: {}'.format(x))
    print('Built-in: {}'.format(dir))


print(scope_demo())

# multiple parameters


def add_two_nums(a, b):
    return a + b


print(add_two_nums(2, 8))
print(add_two_nums(2.4, 5.7))
print(add_two_nums('4', '6'))

# default parameters


def add_n(num, n=3):
    'default to adding 3'
    return num + n


print(add_n(2))
print(add_n(15, -5))

# not a great idea to use mutable types as default parameters


def to_list(value, default=[]):
    default.append(value)
    return default


print(to_list(4))
print(to_list('hello'))

# instead, write it this way using 'None'


def to_list2(value, default=None):
    if default is None:
        default = []
    default.append(value)
    return default


print(to_list2(4))
print(to_list2('hello'))


# EXERCISES

# 1
def is_odd(num):
    if num % 2 == 0:
        odd = False
    else:
        odd = True
    return odd


print(is_odd(5))

# 2


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, 'is not a prime number')
                print(i, 'times', num // i, 'is', num)
                break
        else:
            print(num, 'is a prime number')
    elif num < 1:
        print('please input a positive number')
    else:
        print(num, 'is a prime number')


print(is_prime(427))

# 3

from bisect import bisect_left


def binary_search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


a = [1, 2, 4, 4, 8]
x = int(4)
res = binary_search(a, x)
if res == -1:
    print(x, 'is absent')
else:
    print('First occurrence of', x, 'is present at', res)

# 4
i = None


def get_indices(string):
    for i, c in enumerate(string):
        if c.isupper():
            return [i, c]


print(get_indices('Hello'))

# def get_indices(s):
#     return [i for i, c in enumerate(s) if c.isupper()]


# get_indices('Hello')


def camel_conversion(test_string):
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in test_string]).lstrip('_')


print(camel_conversion('HelloDarknessMyOldFriend'))
