array = [[2,5,4],[9,0,3]]
print(array)
print(f"Rows: ",len(array))
print(f"Collumn: ",len(array[0]))
print(array[0][1])
print(array[1][2])
for x in array[1]:
    print(x, end=" ")
print()
for x in array[0]:
    print(x, end=" ")
print()
for x in array[1]:
    print(x, end=" ")

print()

print(f"{array[0][-1]}\n{array[1][-1]}")
