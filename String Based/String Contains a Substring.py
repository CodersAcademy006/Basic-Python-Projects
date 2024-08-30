def contains_substring(s, sub):
    return sub in s

# Take input from user
s = input("Enter the main string: ")
sub = input("Enter the substring: ")
print(f"Substring found: {contains_substring(s, sub)}")
