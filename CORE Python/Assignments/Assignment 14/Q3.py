#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
words = ['apple', 'orange', 'apple', 'cherry', 'orange']
unique_words = set(words)

for word in unique_words:
    count = words.count(word)
    print(word, ":", count)
