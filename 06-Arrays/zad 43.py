def identity_matrix(n):
    for row in range(0, n):
        for col in range(0, n):
            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()

identity_matrix(3)
identity_matrix(5)
identity_matrix(8)