def cotojest(array):
    l = len(array)
    line1 = "-" * l * 4 + "-" * (l + 1)
    line2 = "|"
    for x in array:
        if x <= 9:
            line2 = line2 + f"   {x}|"
        elif x > 9 and x <= 99:
            line2 = line2 + f"  {x}|"
        elif x > 99:
            line2 = line2 + f" {x}|"
    print(line1)
    print(line2)
    print(line1)

array = [1, 23, 5, 382, 1, 17, 4, 906]
cotojest(array)