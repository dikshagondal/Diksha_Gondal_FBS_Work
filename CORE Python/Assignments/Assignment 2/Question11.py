#write a program to accept an integer amount  from user and tell  minimum number of notes needed for representing that amount. 
amount = int(input('Enter amount :'))

n500 = amount // 500  #3
amount = amount % 500  #360

n200 = amount // 200  #1
amount = amount % 200  #160

n100 = amount // 100  #1
amount = amount % 100  #60

n50 = amount // 50    #1
amount = amount % 50   #10

n10 = amount // 10   #1

print('500 notes=',n500)
print('200 notes=',n200)
print('100 notes=',n100)
print('50 notes=',n50)
print('10 notes=',n10)