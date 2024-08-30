def count_substring_occurrences(s, sub):
    return s.count(sub)

# Take input from user
s = input("Enter the main string: ")
sub = input("Enter the substring: ")
print(f"Number of occurrences: {count_substring_occurrences(s, sub)}")
