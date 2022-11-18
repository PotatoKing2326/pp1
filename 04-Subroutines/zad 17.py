def f(sentence):
    count = 0
    for char in sentence:
        if char == "e":
            count += 1
    print(count)

f("You never get a chance to make first impression")