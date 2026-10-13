def prime(num, i=2):
    if num < 2:
        return False

    if i == num:
        return True

    if num % i == 0:
        return False

    return prime(num, i + 1)


num = int(input("Enter number: "))

if prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")