def is_circular_prime(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    def rotations(x):
        x_str = str(x)
        return {int(x_str[i:] + x_str[:i]) for i in range(len(x_str))}
    
    return all(is_prime(rot) for rot in rotations(n))

# Take input from user
num = int(input("Enter a number: "))
if is_circular_prime(num):
    print(f"{num} is a Circular Prime.")
else:
    print(f"{num} is not a Circular Prime.")
