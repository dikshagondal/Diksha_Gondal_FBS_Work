str = input('Enter a string:')
count = 0

for ch in str:
    if ch in 'aeiouAEIOU':
        count = count + 1

print('Number of Vowel in a string:',count)        