#write a program to calculate selling prize of book based on cost prize and discount.
cp = float(input('Enter cost prize:'))
discount = float(input('Enter discount percentage:'))

discount_amount = cp * discount / 100
sp = cp - discount_amount

print('Selling prize=',sp)