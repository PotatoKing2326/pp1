import re
file = open("testfile.txt", 'r')
content = file.read()
long_word = re.findall(".{6}", content)
for x in long_word:
    print(x)
file.close()