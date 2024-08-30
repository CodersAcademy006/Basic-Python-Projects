def is_palindromic_prime(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    def is_palindrome(x):
        return str(x) == str(x)[::-1]
    
    return is_prime(n) and is_palindrome(n)

# Take input from user
num = int(input("Enter a number: "))
if is_palindromic_prime(num):
    print(f"{num} is a Palindromic Prime.")
else:
    print(f"{num} is not a Palindromic Prime.")
