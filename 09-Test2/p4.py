def f(dictionary,x,y):
    suma = 0
    for key in dictionary:
        value = dictionary[key]
        for integer in value:
            if integer not in range(x,y+1): continue
            else: suma += integer

    return suma

f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6)