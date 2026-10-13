#Python Program to Find the Second Largest Number in a List Using Bubble Sort.
def bubbleSort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size - 1):
            if(li[j] > li[j + 1]):
                li[j], li[j + 1] = li[j +1], li[j]
                

li = [50, 40, 30, 20, 10]

bubbleSort(li)
print(li)
print('Second largest:',li[-2])

