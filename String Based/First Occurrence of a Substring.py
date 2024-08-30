def first_occurrence(s, sub):
    return s.find(sub)

# Take input from user
s = input("Enter the main string: ")
sub = input("Enter the substring: ")
print(f"First occurrence index: {first_occurrence(s, sub)}")
