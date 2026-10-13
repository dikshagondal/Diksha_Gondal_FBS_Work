str = "python"

new = ""

for i in range(len(str)):
    if i == 0:
        new = new + str[len(str) - 1]
    elif i == len(str) - 1:
        new = new + str[0]
    else:
        new = new + str[i]

print(new)