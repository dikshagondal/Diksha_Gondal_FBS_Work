#Python Program to Check if a Given Key Exists in a Dictionary or Not.
d = {"name": "Diksha", "age": 23, "city": "Pune"}

key = input("Enter key: ")

if key in d :
    print("Key exists")
else:
    print("Key does not exist")