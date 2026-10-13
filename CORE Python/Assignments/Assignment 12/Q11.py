str = input('Enter string:')
count = 0

for ch in str:
    if ch.islower():
        count += 1

print('Number of lowercase characters:',count)        
