import re
def f(first_letter,last_letter):
    f = open("data.txt", 'r')
    txt = f.read()
    print(txt)
    f.close()

f("w", "d")