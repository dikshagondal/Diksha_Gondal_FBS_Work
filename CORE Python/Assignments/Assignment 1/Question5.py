#write a program to calculate compound interest.

p = int(input('Enter Principle amount:'))
r = int(input('Enter Rate of interest:'))
t = int(input('Enter Time:'))

ci = p * (1 + r / 100) ** t - p # ci formula

print('Compound Interest =',ci)