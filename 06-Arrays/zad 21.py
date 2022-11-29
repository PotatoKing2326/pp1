def compare(array1, array2):
    count1 = len(array1)
    count2 = len(array2)
    if count1 == count2:
        for x in range(0, count1):
            if array1[x] != array2[x]:
                return False 
    else:
        return False
    return True

a1 = ["water", "book", "sky"]
a2 = ["water", "book", "sky"]

print(compare(a1, a2))