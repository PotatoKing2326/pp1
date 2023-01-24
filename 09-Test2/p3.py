def f(array2D):
    array1D = []
    col = len(array2D[0])
    for x in range(0,col):
        column = 0    
        for d1 in array2D:
            column += d1[x]
        array1D.append(column)

    return array1D
    
        
f(([ [3,6,2,7], [9,5,4,0], [2,8,0,9]]))