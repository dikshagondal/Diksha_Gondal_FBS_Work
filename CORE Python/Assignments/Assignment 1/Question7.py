# program to find the roots of a quadratic equation .

a = int(input('Enter value:'))
b = int(input('Enter value:'))
c = int(input('Enter value:'))

d = b * b - 4*a*c    

root1 = (-b + d ** 0.5) / (2 * a)
root2 = (-b - d ** 0.5) / (2 * a)

print ('Root 1 =' ,root1)
print ('Root 2 =' ,root2)

