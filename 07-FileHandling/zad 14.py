name = str(input("Enter file name: "))
suma = 0
with open(f"{name}", 'r') as f:
    for line in f:
        suma += 1
print(f"Number of lines: {suma}")
f.close()