#write a program to input all sides of triangle and check whether it is valid or not.
a = int(input('Enter first side:'))
b = int(input('Enter second side:'))
c = int(input('Enter third side:'))

if a + b > c and b + c > a and a + c > b :
    print('Triangle is valid.')

else:
    print('Triangle is not valid.')