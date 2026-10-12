area = int(input('Enter area of one wall:'))
interior_cost = int(input('Enter cost of interior wall painting:'))
exterior_cost = int(input('Enter cost of exterior wall painting:'))

interior_total = 2 * area * interior_cost
exterior_total = 6 * area * exterior_cost

total_cost = interior_total + exterior_total

print('Interior painting cost=', interior_total)
print('Exterior painting cost=', exterior_total)
print('Total painting cost=', total_cost)