def is_fermat_prime(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    if n < 3:
        return False
    k = 0
    while 2 ** k - 1 < n:
        k += 1
    return n == 2 ** (2 ** k) + 1 and is_prime(n)

# Take input from user
num = int(input("Enter a number: "))
if is_fermat_prime(num):
    print(f"{num} is a Fermat prime.")
else:
    print(f"{num} is not a Fermat prime.")
