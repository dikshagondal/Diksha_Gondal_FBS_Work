#input 5 subject marks from user and display grade.
m1 = int(input('Enter marks of subject 1:'))
m2 = int(input('Enter marks of subject 2:'))
m3 = int(input('Enter marks of subject 3:'))
m4 = int(input('Enter marks of subject 4:'))
m5 = int(input('Enter marks of subject 5:'))

total_marks = m1 + m2 + m3 + m4 + m5
percentage = total_marks / 5

print('percentage:',percentage)

if percentage >= 90:
    print('Grade A')
elif percentage >= 75 :
    print('Grade B')
elif percentage >= 60 :
    print('Grade C') 
elif percentage >= 50:
    print('Grade D') 
else:
    print('Grade F')             

