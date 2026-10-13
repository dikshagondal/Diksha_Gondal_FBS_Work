str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagram")
else:
    for ch in str1:
        if ch not in str2:
            print("Not Anagram")
            break
    else:
        print("Anagram")