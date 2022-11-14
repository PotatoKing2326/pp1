import random

dice = random.randint(1, 6)

x = int(input("Enter the number between 1 to 6: "))

if x == dice:
    print(True)
else:
    print(False)