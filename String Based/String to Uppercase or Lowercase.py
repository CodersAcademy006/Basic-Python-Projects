def convert_case(s):
    return s.upper(), s.lower()

# Take input from user
s = input("Enter a string: ")
upper_case, lower_case = convert_case(s)
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")
