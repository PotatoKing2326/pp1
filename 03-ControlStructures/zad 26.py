x = "0805"
t = 0
while t < 3:
    y = str(input("Enter the PIN code: "))
    if x != y:
        print("Incorrect...")
        t += 1
    else:
        break

if t == 3:
    print("Sorry, your payment has been blocked.")

    