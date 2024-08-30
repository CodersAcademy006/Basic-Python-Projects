def largest_prime_factor(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    largest = None
    while n % 2 == 0:
        largest = 2
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest = i
            n //= i
    if n > 2:
        largest = n
    return largest

# Take input from user
num = int(input("Enter a number: "))
print(f"The largest prime factor of {num} is {largest_prime_factor(num)}.")
