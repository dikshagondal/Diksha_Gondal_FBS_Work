def digit_sum(num):
    if num == 0:
       return 0

    
    d = num % 10
    return d + digit_sum(num // 10)
        
    

num = int(input('Enter number:')) 

print('Sum of digits of numbers :',digit_sum(num))