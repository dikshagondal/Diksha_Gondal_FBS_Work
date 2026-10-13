#Write a Python program to remove the intersection of a second set with a first set.
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50 ,60}

common = s1.intersection(s2)
s1.difference_update(common)

print(s1)