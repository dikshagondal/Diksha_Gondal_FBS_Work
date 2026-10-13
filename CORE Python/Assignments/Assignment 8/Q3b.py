def sum_fact(n):
    sum = 0
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        sum = sum + fact
    return sum

n = int(input('Enter number:'))   

print('Sum of factorial:',sum_fact(n))