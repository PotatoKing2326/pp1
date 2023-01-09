f = open("testfile.txt", 'r')
suma = 0
for line in f:
    if suma <= 4:
        print(line, end="")
        suma += 1
    else:
        suma = 0
        input("Press Enter to continue...")
f.close()