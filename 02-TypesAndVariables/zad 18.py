a = int(input("Write first side: "))
b = int(input("Write second side: "))
c = int(input("Write third side: "))

import math

p = (a + b + c)/2
area = math.sqrt(p*(p - a)*(p - b)*(p - c))

print(f"Area of triangle has value: {area}")
