#Python Program to Sort the List According to the Second Element in Sublist.
li = [[1, 5], [2, 3], [3, 8], [4, 2]]

li.sort(key=lambda x: x[1])

print(li)