#write a program to calculate profit or loss.
cp = float(input('Enter cost prize:'))
sp = float(input('Enter selling prize:'))

if (cp > sp):
    profit = cp - sp
    print('Profit : ',profit)

elif(sp > cp):
    loss = sp - cp
    print('Loss :',loss)

else:
    print('No profit, No loss')    
