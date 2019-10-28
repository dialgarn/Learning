# reading a file
# passwd_file = open('password.txt')
# print(passwd_file.readline())
# passwd_file.close

# reading binary files
# binary_passwd_file = open('password.txt', 'rb')
# print(binary_passwd_file.read())
# binary_passwd_file.close

# iteration with files
# the method below is not fantastic: it can eat up memory
# fin = open('password.txt')
# for line in fin.readlines():
#    print(line)
# fin.close
# don't use 'readlines' method
# fin = open('password.txt')
# for line in fin:
#    print(line)
# fin.close

# writing files
fout = open('writing_practice.txt', 'w')
fout.write('George\nAlex\nJeff\nFrank')
fout.close

# writing:
with open('writing_practice2.txt', 'w') as fout2:
    fout2.write('Ringo')
# is the equivalent of:
fout2 = open('writing_practice2.txt', 'w')
fout2.write('Ringo')
fout2.close

# designing around files
# inserting the line number before every line
# can be done this way:


def add_numbers(filename):
    results = []
    with open(filename) as fin:
        for num, line in enumerate(fin):
            results.append('{0}-{1}'.format(num, line))
    return results

# can also be done this way
# should be done this way if you want to reuse some of the code
# this way you aren't depending on a file name


def add_numbers2(filename):
    with open(filename) as fin:
        return add_nums_to_seq(fin)


def add_nums_to_seq(seq):
    results = []
    for num, line in enumerate(seq):
        results.append('{0}-{1}'.format(num + 1, line))
    return results


bleh = [0, 1, 2, 3]
# print(add_nums_to_seq(bleh))
# print(add_numbers2('numbers.txt'))

# EXERCISES


def write_csv_file(filename):
    with open(filename, 'w') as fin:
        return write_csv(fin)


def write_csv(info):
    for i in info:
        return print(i)


a = [('what', 'is', 'popping', 10), ('I do not know', 15)]
write_csv([a])
print(a[0])

test = open('writing_practice2.txt', 'w')
