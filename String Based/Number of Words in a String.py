def count_words(s):
    return len(s.split())

# Take input from user
s = input("Enter a string: ")
print(f"Number of words: {count_words(s)}")
