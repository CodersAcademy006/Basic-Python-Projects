def is_palindrome(s):
    return s == s[::-1]

# Take input from user
s = input("Enter a string: ")
print(f"String is a palindrome: {is_palindrome(s)}")
