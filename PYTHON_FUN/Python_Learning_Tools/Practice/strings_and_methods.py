
# can be invoked through a variable or directly (on a string literal)
# name = 'matt'
# correct = name.capitalize()
# print(correct)
# print(name)
# print('fred'.capitalize())

# endswith and startswith fun
yuh = 'Strings.py'
print(yuh.endswith('.py'))
print(yuh.endswith('.exe'))
print(yuh.endswith('py'))
print(yuh.endswith('y'))
print(yuh.endswith('p'))
print('asdfghjkl')
# 0 refers to the first character and includes it. 7 does not include the 7th character - it refers to the character before the 7th
print(yuh.endswith('Strings', 0, 7))
print(yuh.startswith('Str'))

# find method        returns the index value where the substring begins; otherwise if not found it returns -1
word = 'grateful'
print(word.find('ate'))
print(word.find('great'))

# more format method
print('{} {} {} {} {}'.format(
    'hello',
    'to',
    'you',
    'and',
    'you'
))

# join method
# inserts the string before the method in between the strings in the list
print(',(haha) '.join(['1', '2', '3']))

# lower method

fname = 'readme.txt'
print(fname.endswith('txt')) or (fname.endswith('TXT'))
# the more pythonic way would be to:
# could also be used with the upper method if you wanted to
print(fname.lower().endswith('txt'))

# strip method
print('   hello there  ')
# strips preceding and trailing whitespace (spaces, tabs, newlines)
print('   hello there  '.strip())
print('   hello there  '.lstrip())  # left strip - strips just the preceding
print('   hello there  '.rstrip())  # right strip - strips just the trailing

# EXERCISES

# 1
school = 'Helmers Elementary School'
# print(dir(school))

# 2
country = 'usa'
correct_country = country.upper()
print(correct_country)

# 3
filename = 'hello.py'
print(filename.endswith('.java'))
print(filename.find('py'))
print(filename.startswith('world'))

# 4      use the REPL for this; printing this out here just clogs the console; in REPL use ENTER to 'scroll' through the documentation
# print(help('STRINGMETHODS'))
