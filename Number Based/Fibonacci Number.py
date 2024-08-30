import math

def is_fibonacci(n):
    if n < 0:
        return False
    # A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Take input from user
num = int(input("Enter a number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")
