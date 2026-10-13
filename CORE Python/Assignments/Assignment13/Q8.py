#Python Program to Count the Frequency of Words Appearing in a String Usinga Dictionary.
str = "apple banana apple orange banana"
d = {}

for word in str.split():
    if word in d:
        d[word] = d[word] + 1

    else:
        d[word] = 1

print(d)            