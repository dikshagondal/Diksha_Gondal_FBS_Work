# write program to calculate the percentage of student based on marks of any 5 subject .

subject1 = int(input('Enter marks of subject 1:'))
subject2 = int(input('Enter marks of subject 2:'))
subject3 = int(input('Enter marks of subject 3:'))
subject4 = int(input('Enter marks of subject 4:'))
subject5 = int(input('Enter marks of subject 5:'))

total = subject1 + subject2 + subject3 + subject4 + subject5
percentage = total / 500 * 100
Total_Marks = total

print('Total_Marks:'+str(total))
print('Percentage:'+str(percentage))
print(f'percentage of 5 subject is {percentage}')
