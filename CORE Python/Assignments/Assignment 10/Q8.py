#Write a program to create a duplicate of an existing list. It should not point to same list.

li = [10, 20, 30, 40, 50]
new_list = []

for i in range(len(li)):
    new_list = new_list + [li[i]]


print('Original list:', li)   
print('New list:',new_list) 