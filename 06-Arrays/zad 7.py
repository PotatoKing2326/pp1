array = [1, 2, 3, 4, 5]
print(array)
array[0] -= 1
print(array)
array[-1] += 4
print(array)
array[len(array)//2] *= 2
print(array)
for x in range(len(array)):
    array[x] += 3
print(array)