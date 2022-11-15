x = int(input("x = "))
y = int(input("y = "))

if x == 0 and y == 0:
    print(f"Point P({x}, {y}) is in the center of coordinate system.")
elif x == 0 and y != 0:
    print(f"Point P({x}, {y}) is in the 'y' axis of coordinate system.")
elif x != 0 and y == 0:
    print(f"Point P({x}, {y}) is in the 'x' axis of coordinate system.")
elif x < 0:
    if y > 0:
        print(f"Point P({x}, {y}) is in the second quadrant axis of coordinate system.")
    elif y < 0:
        print(f"Point P({x}, {y}) is in the third quadrant axis of coordinate system.")
elif x > 0:
    if y > 0:
        print(f"Point P({x}, {y}) is in the first quadrant axis of coordinate system.")
    elif y < 0:
        print(f"Point P({x}, {y}) is in the fourth quadrant axis of coordinate system.")