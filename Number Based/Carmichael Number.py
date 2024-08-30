from sympy import isprime

def is_carmichael(n):
    if n < 2:
        return False
    if any(n % p == 0 for p in range(2, int(n**0.5) + 1) if isprime(p)):
        return False
    for a in range(2, n):
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Take input from user
num = int(input("Enter a number: "))
if is_carmichael(num):
    print(f"{num} is a Carmichael number.")
else:
    print(f"{num} is not a Carmichael number.")
