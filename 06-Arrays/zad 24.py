array = [2, 3, 2, 5, 8, 1, 9, 8]
array2 = array
unique = set(array) # [2, 3, 5, 8, 1, 9]
for x in unique:
    count = 0
    for y in array:
        if y == x:
            count += 1
    if count > 1:
        for remove in range(count):
            array2.remove(x)

print(array2)