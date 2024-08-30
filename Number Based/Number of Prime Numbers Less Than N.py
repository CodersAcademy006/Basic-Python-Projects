def count_primes_less_than(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    return sum(1 for i in range(2, n) if is_prime(i))

# Take input from user
num = int(input("Enter a number: "))
print(f"The number of prime numbers less than {num} is {count_primes_less_than(num)}.")
