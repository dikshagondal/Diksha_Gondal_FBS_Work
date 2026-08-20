#convert distance given in feet and inches into meter and centimeter.

feet = int(input('Enter feet:'))
inches = int(input('Enter inches'))

total_inches = feet * 12 + inches
meters = total_inches * 0.0254
centimeters = total_inches * 2.54

print('Distance in meters =',meters)
print('Distance in centimeters =',centimeters)