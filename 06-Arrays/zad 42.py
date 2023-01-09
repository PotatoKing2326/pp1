def swapper(array):
    r =""
    print("Arrau after changes: ")
    for x in range(0, 3):
        r += str(array[x][-1]) + " "
        for y in range(1,4):
            r += str(array[x][y]) + " "
        r += str(array[x][0]) + " "
        print(r)
        r = ""

array = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]

print("Array before changes: ")
for x in array:
    for y in x:
        print(y,end = " ")
    print()

swapper(array)