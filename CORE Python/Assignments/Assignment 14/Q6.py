#Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pair = set()
max_product = 0

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        product = li[i] * li[j]

        if product > max_product:
            max_product = product
            pair = {li[i], li[j]}

print('pair:',pair)            