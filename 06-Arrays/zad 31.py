def seperator(array):
    even = []
    odd = []
    for x in array:
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    print(f"Even: {even}")
    print(f"Odd: {odd}")

array = [1, 2, 4, 6, 3, 6, 7, 5]
seperator(array)