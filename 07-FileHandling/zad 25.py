import re
txt = "To be, or not to be, that is the question"
vowels = re.findall("\s", txt)
ilosc = len(vowels) + 1
print(ilosc)