def armstrong(num, temp, count, sum):
    if temp == 0:
        return sum == num

    d = temp % 10
    sum = sum + d ** count
    return armstrong(num, temp // 10, count, sum)

num = int(input('Enter number:'))

temp = num
count = 0

while temp > 0:
    count += 1
    temp = temp // 10

if armstrong(num, num, count, 0):
    print(f'{num} is an armstrong number.')  
else:
    print(f'{num} is not an armstrong number.')      

 

    