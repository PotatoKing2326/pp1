def swapper(array):
    r1 = array[0]
    r3 = array[2]
    array[0] = r3
    array[2] = r1
    print("Array after changes: ")
    for x in array:
        for y in x:
            print(y,end = " ")
        print()
array = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]

print("Array before changes: ")
for x in array:
    for y in x:
        print(y,end = " ")
    print()

swapper(array)