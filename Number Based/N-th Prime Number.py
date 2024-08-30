def nth_prime(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    count, num = 0, 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

# Take input from user
n = int(input("Enter the position of the prime number to find: "))
print(f"The {n}-th prime number is {nth_prime(n)}.")
