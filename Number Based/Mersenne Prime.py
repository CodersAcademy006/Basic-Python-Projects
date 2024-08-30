def is_mersenne_prime(p):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    mersenne_number = 2 ** p - 1
    return is_prime(p) and is_prime(mersenne_number)

# Take input from user
p = int(input("Enter a number (p) to check if 2^p - 1 is a Mersenne prime: "))
if is_mersenne_prime(p):
    print(f"2^{p} - 1 is a Mersenne prime.")
else:
    print(f"2^{p} - 1 is not a Mersenne prime.")
