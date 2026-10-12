p1 = int(input('Enter price of product 1:'))
p2 = int(input('Enter price of product 2:'))
p3 = int(input('Enter price of product 3:'))
p4 = int(input('Enter price of product 4:'))
p5 = int(input('Enter price of product 5:'))

total = p1 + p2 + p3 + p4 + p5
gst = total * 18 / 100
bill = total + gst
print(gst)
print('Total_bill:',bill)