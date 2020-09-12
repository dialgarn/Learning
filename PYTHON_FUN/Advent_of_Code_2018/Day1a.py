fin = open("frequency_list2.txt")
num_list = []
for line in fin:
    num_list.append(line)

fin.close
new_list = []
for val in num_list[:-1]:
    new_list.append(val[:-1])

new_list.append(num_list[-1])
final_sum = 0
for val in new_list:
    final_sum += int(val)

print(final_sum)


def frequency_sum(filename):
    # takes input from a file and sums up the values
    numList = []
    newList = []
    finalSum = 0
    fin = open(filename)
    for line in fin:
        numList.append(line)
    fin.close
    for val in numList[:-1]:
        newList.append(val[:-1])
    newList.append(numList[-1])
    for val in newList:
        finalSum += int(val)
    return finalSum


print(frequency_sum('frequency_list.txt'))
print(frequency_sum('frequency_list2.txt'))
# print(frequency_sum('numbers.txt'))


# Part B
temp_sum = 0
sum_list = []
for val in new_list:
    temp_sum += int(val)
    sum_list.append(temp_sum)
