s1 = {1, 2, 3, 4, 5, 6}
s2 = {3, 4, 5, 6, 7, 8}

missing_in_s2 = s1.difference(s2)
missing_in_s1 = s2.difference(s1)

print('Missing element in set 2:',missing_in_s2)
print('Missing element in set 1:',missing_in_s1)