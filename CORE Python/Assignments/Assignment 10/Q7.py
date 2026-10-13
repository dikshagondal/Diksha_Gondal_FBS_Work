#write a program to create a list from existing list which contain cube of each number of list.
li = [1, 2 , 3, 4, 5]
new_list =[]

for i in range(len(li)):
    cube = li[i] ** 3
    new_list = new_list + [cube]

print('New list:',new_list)    