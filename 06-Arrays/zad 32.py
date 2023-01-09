def string(array):
    string = "String: "
    l = len(array)
    for x in range(0,l):
        if x < l-1:
            string = string + f"{array[x]},"
        else:
            string = string + f"{array[x]}"
    print(string)

array = 5,4,3,2,6,5
string(array)