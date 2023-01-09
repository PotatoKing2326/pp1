file = open("integers.txt", 'w')
integer = 1
for x in range(0, 50):
    file.write(f"{str(integer)}\n")
    integer += 1
file.close()