#Write a program to print all numbers which are divisible by m and n in the list.
li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
m = int(input('Enter m:'))
n = int(input('Enter n:'))

for i in range(len(li)):
    if li[i] % m == 0 and li[i] % n == 0:
        print(li[i])