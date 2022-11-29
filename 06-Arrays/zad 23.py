def swape(tab, l, p):
    temp = tab[l]
    tab[l] = tab[p]
    tab[p] = temp

array = [1, 3, 787, 5, 4, 2]
print(array)
y = len(array)-1
while y > 1:
    for x in range(0, y):
        if array[x] > array[x+1]:
            swape(array, x, x+1)
    y -= 1
print(array)

