#Write a program to check if given number is prime number or not.
num = int(input('Enter number:'))
count = 0

for i in range(1, num + 1):
    if (num  % i == 0):
        count = count + 1
    
if count == 2 :
        print(f'{num} is prime number.')

else:
        print(f'{num} is not prime number')    

