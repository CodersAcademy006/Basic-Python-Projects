def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Take input from user
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
print(f"Strings are anagrams: {are_anagrams(s1, s2)}")
