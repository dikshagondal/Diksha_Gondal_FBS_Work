#write a program to remove duplicates from the list.
li = [10, 20, 30, 40, 30, 50, 60, 10]
new_list = []

for i in range(len(li)):
    count = 0

    for j in range(i):
        if li[i] == li[j]:
            count += 1
    if count == 0:
        new_list = new_list + [li[i]] 

print('New list:',new_list)
