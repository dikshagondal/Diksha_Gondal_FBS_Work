#Write a program to create three lists of numbers, their squares and cubes.
li = [1, 2, 3, 4, 5]
square = []
cube = []

for i in range(len(li)):
    square = square + [li[i] ** 2]
    cube = cube + [li[i] ** 3]

print('Number:',li)
print('Square:',square)
print('Cube:',cube)    
