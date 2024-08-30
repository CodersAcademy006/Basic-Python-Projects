def last_occurrence(s, sub):
    return s.rfind(sub)

# Take input from user
s = input("Enter the main string: ")
sub = input("Enter the substring: ")
print(f"Last occurrence index: {last_occurrence(s, sub)}")
