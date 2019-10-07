status = 'off'
wattage = '120 watt'  # sets wattage
incandescent = wattage  # sets incandescent to the original wattage
wattage = '25 watt'  # setts wattage to a new value

##  print(incandescent, wattage)

# Rebinding Variables

num = 400
num = '400'  # now num is a string

# Naming Variables

# break = 'foo'      #doesn't like it because 'break' is a keyword in python (is considered a syntax error)


# examples of good and bad variable names

# >>> good = 4
# >>> bAd = 5 # bad - capital letters
# >>> a_longer_variable = 6
# this style is frowned upon
# >>> badLongerVariable = 7
# bad - starts with a number
# >>> 3rd_bad_variable = 8
# File "<stdin>", line 1
# 3rd_bad_variable = 8
# ^
# SyntaxError: invalid syntax
# bad - keyword
# >>> for = 4
# File "<stdin>", line 1
# for = 4
# ^
# SyntaxError: invalid syntax
# bad - built-in function
# >>> compile = 5

# Exercises

# 1
pi = 3.141592654
r = 10
print(pi * r**2)

# 2
b = 10
h = 2

# 3
print(2 * b + 2 * h)
b = 6
print(2 * b + 2 * h)
