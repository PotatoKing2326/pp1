array = [15, 8, 31, 47, 2, 19]

line = "existed array: "
for i in array:
    line = line + str(i) + " "
print(line)

line = "reverse array: "
for i in range(5, -1, -1):
    line = line + str(array[i]) + " "
print(line)