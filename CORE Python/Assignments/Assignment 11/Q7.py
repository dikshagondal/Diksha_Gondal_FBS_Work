#Python Program to Find the Intersection of Two Lists.
li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]

intersection = list(set(li1) & set(li2))

print("Intersection:", intersection)