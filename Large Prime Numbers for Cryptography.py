from sympy import primerange

def generate_large_prime(bits):
    primes = list(primerange(2**(bits-1), 2**bits))
    return random.choice(primes)

# Take input from user
bits = int(input("Enter the number of bits for the prime: "))
large_prime = generate_large_prime(bits)
print(f"A large prime number with {bits} bits is {large_prime}.")
