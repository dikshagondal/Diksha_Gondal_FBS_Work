#write a program to convert days into years, weeks and days.

days = int(input('Enter number of days:'))

years = days // 365
remaining_days = days % 365
print('Years=',years)
print('Remaining_days =',remaining_days)