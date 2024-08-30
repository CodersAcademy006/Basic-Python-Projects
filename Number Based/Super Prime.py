def is_super_prime(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    return is_prime(n) and is_prime(sum(int(digit) for digit in str(n)))

# Take input from user
num = int(input("Enter a number: "))
if is_super_prime(num):
    print(f"{num} is a Super Prime.")
else:
    print(f"{num} is not a Super Prime.")
