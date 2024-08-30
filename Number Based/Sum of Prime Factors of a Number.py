def sum_of_prime_factors(n):
    def prime_factors(x):
        factors = []
        for i in range(2, int(x**0.5) + 1):
            while x % i == 0:
                factors.append(i)
                x //= i
        if x > 1:
            factors.append(x)
        return factors
    
    return sum(set(prime_factors(n)))

# Take input from user
num = int(input("Enter a number: "))
print(f"The sum of the prime factors of {num} is {sum_of_prime_factors(num)}.")
