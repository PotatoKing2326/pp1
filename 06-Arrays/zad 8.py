array = [-15, 8, -31, 47, -2, 19]
minimum = array[0]
maximum = array[0]
for x in array:
    if x > maximum:
        maximum = x
    if minimum > x:
        minimum = x

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")