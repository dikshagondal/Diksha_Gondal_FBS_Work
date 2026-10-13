def digit_sum(num):
    sum = 0
    temp = num

    while temp > 0:
        d = temp % 10
        temp = temp // 10
        sum = sum + d

    return sum

num = int(input('Enter number:')) 

print('Sum of digits of numbers :',digit_sum(num))