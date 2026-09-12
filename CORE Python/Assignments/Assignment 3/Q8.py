import random
userID = input('Enter userID:')
password = input('Enter password:')

if userID == '1234' and password == '1234' :
    systemcaptcha = random.randint(1000 ,9999)
    print(systemcaptcha)

    captcha = int(input('Enter the captcha:'))

    if captcha == systemcaptcha:
         print('Successfully log in.')    

    else:
        print('Invalid captcha')

else:
    print('Invalid ID and password.')
    