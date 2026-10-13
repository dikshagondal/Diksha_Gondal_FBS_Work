def area_circle(radius):
    area = 3.14 * radius * radius
    return area

r = int(input('Enter radius: '))

print('Area of circle:',area_circle(r))