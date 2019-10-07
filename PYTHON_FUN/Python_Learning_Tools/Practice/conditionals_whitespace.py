name = 'Matt'
print(name == 'Matt')
print(name != 'Fred')
print(1 > 3)

# have to write out the second 'score'; cant string together conditionals
score = 91
if score > 90 and score <= 100:
    grade = 'A'
else:
    grade = 'F'
print(grade)

# you can string it together this way in a range
if 90 < score <= 100:
    grade = 'lmao you passed'
else:
    grade = 'youre dumb'
print(grade)

name = 'Paul'
beatle = None
if name == 'George' or \
        name == 'Ringo' or \
        name == 'John' or \
        name == 'Paul':
    beatle = True
else:
    beatle = False
print(beatle)

beatles = {'George', 'Ringo', 'John', 'Paul'}
beatle = name in beatles
print(beatle)

# uses the 'not' keyword in a conditional statement
last_name = 'unknown'
if name == 'Paul' and not beatle:
    last_name = 'Revere'
print(last_name)

# else statements
score = 87
if score >= 90:
    grade = 'A'
else:
    grade = 'B'

# same thing with more options; use 'elif' - else if statements
score = 87
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# EXERCISES

# 1
year_list = [1800, 1900, 1903, 2000, 2002, 2020, 3464, 5000, 4912]

for i, val in enumerate(year_list):
    if val % 4 == 0:
        if val % 100 == 0:
            if val % 400 == 0:
                print(val, 'leap year')
            else:
                print(val, 'not a leap year')
        else:
            print(val, 'leap year')
    else:
        print(val, 'not a leap year')

# 2
num_list = [1, 2, 3, 4, 112345]

for i, val in enumerate(num_list):
    if val % 2 == 0:
        print(val, 'even!')
    else:
        print(val, 'odd!')
