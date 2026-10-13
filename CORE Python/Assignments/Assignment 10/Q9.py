#Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.
li = [10, 25, 35, 40, 55, 60, 75, 80]

even_list = []
odd_list = []

for i in range(len(li)):
    if li[i] % 2 == 0:
        even_list = even_list + [li[i]]

    else:
        odd_list = odd_list + [li[i]]

print('Even list:', even_list)
print('Odd list:', odd_list)            