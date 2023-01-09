file1 = open("testfile.txt", 'r')
file2 = open("copylines.txt", 'w')
for line in file1:
    file2.write(line)
file1.close()
file2.close()