# print(1.01 - 0.99)

# print(4%3)

# print(4**2)

# print(10**100)

# print(4 + 2 * 3)        #ORDER OF OPERATIONS - PEMDAS
# print((4 + 2) *3)

# Excercises

# 1
# sleep = (6.2 + 7 + 8 + 5 + 6.5 + 7.1 + 8.5)
# avg_sleep = (sleep / 7)
# print(avg_sleep)

# 2
# num = 297 / 3
# if type(num) == int:
# print('yes')
# else:
# print('no')

# 3
# print(2**10)

# 4
year_list = [1800, 1900, 1903, 2000, 2002, 2020, 3464, 5000]

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
