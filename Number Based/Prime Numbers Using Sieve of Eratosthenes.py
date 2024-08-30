def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    return [p for p in range(limit + 1) if sieve[p]]

# Take input from user
limit = int(input("Enter the upper limit for prime numbers: "))
print(f"Prime numbers up to {limit} are: {sieve_of_eratosthenes(limit)}.")
