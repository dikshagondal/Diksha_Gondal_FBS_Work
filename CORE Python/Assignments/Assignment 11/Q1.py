#Python Program to Put Even and Odd elements of a List into two different lists.
li = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for i in range(len(li)):
    if li[i] % 2 == 0:
        even.append(li[i])
    else:
        odd.append(li[i])

print('Even elements:', even)
print('Odd elements:', odd)