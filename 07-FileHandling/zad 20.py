import random
file = open("random.txt", 'w')
for x in range(0, 50):
    file.write(f"{random.randrange(100, 999)}\n")
file.close()