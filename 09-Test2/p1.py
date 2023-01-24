def f(player1, player2):
    p1 = 0
    p2 = 0
    for x in player1:
        if x == "A" or x == "K" or x == "Q" or x == "J" or x == "T":
            p1 += 10
        else:
            p1 += int(x)
    
    for x in player2:
        if x == "A" or x == "K" or x == "Q" or x == "J" or x == "T":
            p2 += 10
        else:
            p2 += int(x)

    if p1 > p2:
        return True
    else:
        return False

print(f("9532","K8"))