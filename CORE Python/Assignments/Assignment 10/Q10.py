#Write a program to remove all occurrences of a given element in the list.
li = [10, 20, 30, 10, 40, 50]
search = 10
new_list = []

for i in range(len(li)):
    if search != li[i]:
        new_list = new_list + [li[i]]

print('New list:',new_list)

