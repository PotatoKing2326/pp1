def median(array):
    array.sort()
    l = len(array)
    middle = l/2
    if l%2 != 0:
        middle = int(middle)
        print(array[middle])
    else:
        middle = int(middle)
        print((array[middle - 1] + array[middle])/2)

array = [6, 8, 3, 1, 0, 5, 7]
median(array)