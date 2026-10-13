li = [10, 20, 30, 40, 50]

max_num = li[0]
sec_max = li[0]

for ind in range(0, len(li)):
    if li[ind] > max_num:
        sec_max = max_num
        max_num = li[ind]

    elif li[ind] > sec_max :
        sec_max = li[ind]


print('Maximum number:', max_num)
print('second maximum number:', sec_max)                    