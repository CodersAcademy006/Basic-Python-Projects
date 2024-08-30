import random

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    def is_composite(a, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        while d != n - 1:
            x = pow(x, 2, n)
            d *= 2
            if x == n - 1:
                return False
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        if is_composite(a, d, n):
            return False
    return True

# Take input from user
num = int(input("Enter a number: "))
if miller_rabin(num):
    print(f"{num} is likely a prime number.")
else:
    print(f"{num} is not a prime number.")
