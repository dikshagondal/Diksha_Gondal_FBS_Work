def palindrome(num):
    original = num
    rev = 0

    while num > 0:
        d = num % 10
        num = num // 10
        rev = rev * 10 + d

    if original == rev :
       return True

    else:
        return False
    
num = int(input('Enter number:'))

print(palindrome(num))