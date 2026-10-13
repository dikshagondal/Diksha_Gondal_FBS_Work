str = "Python"
nth = 2

str1 = ""

for i in range(len(str)):
    if i != nth:
        str1 = str1 + str[i]

print(str1)