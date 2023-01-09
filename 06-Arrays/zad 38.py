def create_2d_array(x,y):
    small_array = [0] * y
    big_array = [small_array] * x
    for x in big_array:
        for y in x:
            print(y,end = " ")
        print()

create_2d_array(3, 5)