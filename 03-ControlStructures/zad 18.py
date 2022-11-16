x = int(input("Enter amount in PLN: "))
x2 = x
zl1 = 0
zl2 = 0
zl5 = 0
while x >= 5:
    x -= 5
    zl5 += 1
while 1 < x < 5:
    x -= 2
    zl2 += 1
while 0 < x < 2:
    x -= 1
    zl1 += 1

print(f"The amount of PLN {x2} in coins: \n5 zł - {zl5} \n2 zł - {zl2} \n1 zł - {zl1} \n")

