f = open("frequency_list.txt", "r")
x = f.readlines()
f.close()
print(x.sum())
