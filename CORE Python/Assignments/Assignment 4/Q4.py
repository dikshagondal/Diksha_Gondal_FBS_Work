#write a program to print fibonacci series upto n.
n = int(input('How many fibonacci numbers you want.'))
a = -1
b = 1
for i in range(1, n + 1):
    c = a + b
    a = b
    b = c

    print(c, end =  " ")