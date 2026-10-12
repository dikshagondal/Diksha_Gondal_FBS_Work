for i in range(1, 11):
    for j in range(1, 22):
        if i == 1 or i == 10 or j == 21 - int((i - 1) *  21 / 10):
            print("*", end="")
        else:
            print(" ", end="")
    print()
