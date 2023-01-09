file = open("power.txt", 'w')
for x in  range(1,10):
    file.write(f"{x},{x**2},{x**3}\n")
file.close()