#Python Program to Multiply All the Items in a Dictionary.
d = {'a' : 10, 'b' : 20, 'c' : 30}
result = 1

for value in d.values():
    result = result * value

print(result)    
