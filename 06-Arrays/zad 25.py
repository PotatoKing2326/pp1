def occurs(number, array):
    if number in array:
        return True

number = int(input("Enter number: "))
array = [15, 38, 7, 23, 14]

ret = occurs(number, array)
if ret == True:

    print(f"Number: {number}\nArray: {array}\nResult: number {number} appears in array")


