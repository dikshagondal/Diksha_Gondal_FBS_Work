#Write a program to find the sum of all elements of a list.
li = [10, 20, 30, 40, 50]
sum = 0

for ind in range(0, len(li)):
    sum = sum + li[ind]
print('Sum of elements of list is:', sum)