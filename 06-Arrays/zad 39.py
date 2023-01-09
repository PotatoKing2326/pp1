array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def multiplication_table(array):
    l1 = 1
    l2 = 2
    l3 = 3
    l4 = 4
    l5 = 5
    for x in range(0, 5):
        if x == 0:
            for y in range(0,5):
                array[x][y] = l1
                l1 += 1
        if x == 1:
            for y in range(0,5):
                array[x][y] = l2
                l2 += 2
        if x == 2:
            for y in range(0,5):
                array[x][y] = l3
                l3 += 3
        if x == 3:
            for y in range(0,5):
                array[x][y] = l4
                l4 += 4
        if x == 4:
            for y in range(0,5):
                array[x][y] = l5
                l5 += 5
    for x in array:
        for y in x:
            print(y,end = " ")
        print()
multiplication_table(array)