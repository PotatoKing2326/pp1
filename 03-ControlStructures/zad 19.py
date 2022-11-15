x = int(input("Enter the dog's age in human's years: "))
if x <= 2:
    age = x * 10.5
else:
    x = x - 2
    age = (2 * 10.5) + x * 4
print(f"The dog's age in dog's years is {age} years.")