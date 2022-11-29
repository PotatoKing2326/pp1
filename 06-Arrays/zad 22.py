a2 = [5, 1, 36]
a1 = [4, 36, 12, 28,9, 44, 5]

for x1 in a1:
    willShow = True
    for x2 in a2:
        if x1 == x2:
            willShow = False
    if willShow == True:
        print(x1)