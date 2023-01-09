array = [[2,3],[1,5]]
def convert(array):
    array2 = []
    for x in array:
        for y in x:
            array2.append(y)

    print(array2)

convert(array)