import re
file = open("grades.txt", 'r')
content = file.read()
grades = re.findall("\d+\.\d+", content)
quantity = len(grades)
suma = 0
for x in grades:
    suma += float(x)
mean = suma / quantity
print(mean)
file.close()