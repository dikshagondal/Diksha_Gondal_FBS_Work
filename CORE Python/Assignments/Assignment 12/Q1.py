#
str = 'banana'
str1 = ''

for ch in str:
    if ch == 'a':
        str1 = str1 + '$'

    else:
        str1 = str1 + ch

print(str1)            