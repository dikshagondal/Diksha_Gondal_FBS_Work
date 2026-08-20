#convert the time entered in hh, min and sec into seconds.

h = int(input('Enter hours:'))
m = int(input('Enetr minutes:'))
s = int(input('Enter seconds:'))

total = (h * 3600) + (m * 60) + s

print('Total_Seconds=',total)