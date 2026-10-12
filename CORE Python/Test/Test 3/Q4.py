n = int(input('Enter number of employee:'))


all_salary = 0

for i in range(1, n + 1):

    basic = int(input("Enter basic salary: "))

    if basic < 20000:
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    total = basic + da + ta + hra

    print("Total salary =", total)

    all_salary = all_salary + total

print("Total salary of all employees =", all_salary)
