array = [12, 6, 4, 9, 10]
def star(n):
    line = ""
    count = array[n]
    for x in range(0, count+1):
        line = line + "*"
    print(f"{count}: {line}")

star(0)