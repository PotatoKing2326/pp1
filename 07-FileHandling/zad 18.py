maf = open("MeatAndFish.txt", 'r')
gab = open("GrainsAndBread.txt", 'r')
shoppinglist = open("shoppinglist.txt", 'w')
for line in maf:
    shoppinglist.write(line)
for line in gab:
    shoppinglist.write(line)
maf.close()
gab.close()
shoppinglist.close()