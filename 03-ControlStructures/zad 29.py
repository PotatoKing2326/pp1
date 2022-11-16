q = 0
n = int(input("Enter number: "))
s = n
while n != 0:
    n = int(input("Enter number: "))
    q += 1
    s += n

m = int(s/q)

print(f"RESULT: Quantity={q}, Sum={s}, Mean={m}")