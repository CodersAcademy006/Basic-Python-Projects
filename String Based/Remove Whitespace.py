def remove_whitespace(s):
    return s.replace(" ", "")

# Take input from user
s = input("Enter a string: ")
print(f"String with whitespace removed: {remove_whitespace(s)}")
