def sum_of_n_primes(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    primes, num, total = [], 2, 0
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
            total += num
        num += 1
    return total

# Take input from user
n = int(input("Enter the number of prime numbers to sum: "))
print(f"The sum of the first {n} prime numbers is {sum_of_n_primes(n)}.")
