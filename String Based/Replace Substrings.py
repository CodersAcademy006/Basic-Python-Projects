def replace_substring(s, old, new):
    return s.replace(old, new)

# Take input from user
s = input("Enter the string: ")
old = input("Enter the substring to replace: ")
new = input("Enter the new substring: ")
print(f"String after replacement: {replace_substring(s, old, new)}")
