#find the sum of three-digit number
num = int(input('Enter three digit number:'))

digit1 = num // 100
print('Digit1=',digit1)

digit2 = (num // 10) % 10
print('Digit2=',digit2)

digit3 = num % 10
print('Digit3=',digit3)

sum = digit1 + digit2 + digit3
print('Sum of digits =',sum)