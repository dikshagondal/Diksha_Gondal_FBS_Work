#Python Program to Remove the Given Key from a Dictionary.
d = {"a": 10, "b": 20, "c": 30}

key = input("Enter key to remove: ")

d.pop(key)

print(d)