import re
txt = "To be, or not to be, that is the question"
vowels = re.findall("[eoaiu]", txt)
ilosc = len(vowels)
print(ilosc)