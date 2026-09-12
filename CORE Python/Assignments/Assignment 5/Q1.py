correct_id = 'Diksha@123'
correct_password = 'Diksha_123'
count = 1
while count <= 3:
    user_id = input('Enter user_id:')
    password = input('Enter password:')

    if user_id == correct_id and correct_password == password:
        print('login successful.')
        break

    else:
        print('Incorrect userid or password.')

        count = count + 1
if count > 3 :
    print('attempt completed.')     
                            