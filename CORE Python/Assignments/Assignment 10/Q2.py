li = [10, 20, 30, 40, 50]

max_num = li[0]
min_num = li[0]

for ind in range(1, len(li)):
    if li[ind] > max_num:
        max_num = li[ind]

    elif li[ind] < min_num :
        min_num = li[ind]

print('Maximum number:', max_num)
print('Minimum number:', min_num)                    