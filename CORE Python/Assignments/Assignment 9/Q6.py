def fibbo_series(n, a, b):
    if n == 0:
        return

    c = a + b
    print(c, end=' ')

    fibbo_series(n - 1, b, c)


n = int(input("Enter number: "))

fibbo_series(n, -1, 1)