#write a program to check if user has entered correct userid and password.
userID = input('Enter userID :')
password = input('Enter password :')

if userID == 'Diksha@123' and password == '1234':
    print('valid user')

else:
    print('Invalid userID and password')    