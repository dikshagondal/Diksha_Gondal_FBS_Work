#Write a Python program to find the longest common prefix of all strings. UsenPython set.
li = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(li[0])):
    s = set()

    for word in li:
        s.add(word[i])

    if len(s) == 1:
        prefix = prefix + li[0][i]
    else:
        break

print(prefix)