array = [[-38, 19], [5,40], [-7,11], [29,16]]
def finder(array):
    smallest = array[0][0]
    largest = array[0][0]
    for x in array:
        for y in x:
            if y < smallest:
                smallest = y
            if y > largest:
                largest = y

    print(f"Smallest: {smallest}\nLargest: {largest}")

finder(array)