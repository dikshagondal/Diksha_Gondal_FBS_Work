#write a program to calculate simple interest

p = int(input('Enter Principle amount:'))
r = int(input('Enter Rate of interest:'))
t = int(input('Enter Time:'))

si = p * r * t / 100

print('Simple Interest =',si)