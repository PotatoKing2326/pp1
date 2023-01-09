array = [4, 2, 8, 4, 7, 9, 5]
def minmax(array):
    array.sort()
    array2 = [array[0], array[-1]]
    print(array2)

minmax(array)