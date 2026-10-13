li = [10, 20, 30, 50, 40, 50, 70, 80]
num = int(input('Enter number:'))
count = 0
for ind in range(0, len(li)):
    if li[ind] == num:
        count = count + 1

if count == 0:
        print(f'{num} is not present in the list.')

else:
        print(f'{num} is present {count} times in the list')        
