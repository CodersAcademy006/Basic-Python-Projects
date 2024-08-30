def to_camel_case(s):
    parts = s.split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

# Take input from user
s = input("Enter a string: ")
print(f"Camel case string: {to_camel_case(s)}")
