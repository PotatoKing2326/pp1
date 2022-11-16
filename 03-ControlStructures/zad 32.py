def f(n):
    for x in range(1,n+1):
        y = x
        l = ""
        for x in range(1, n+1):
            l += str(y) + " "
            y += n
        print(l)    

f(8)    