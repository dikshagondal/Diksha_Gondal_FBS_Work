for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or i == 1 or i + j == 6 :
            print(i + j - 1, end = ' ')
        else:
            print(' ', end = ' ')

    print()            