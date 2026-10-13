str = input('Enter a string:')
character = 0
words = 1

for ch in str:
    character += 1

    if ch == " ":
        words += 1

print("Number of characters:",character)
print("Number of words:",words)    