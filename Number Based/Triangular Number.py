import math

def is_triangular(n):
    if n < 0:
        return False
    # Solve x^2 + x - 2*n = 0
    discriminant = 1 + 8 * n
    root = math.isqrt(discriminant)
    return root * root == discriminant and (root - 1) % 2 == 0

# Take input from user
num = int(input("Enter a number: "))
if is_triangular(num):
    print(f"{num} is a Triangular number.")
else:
    print(f"{num} is not a Triangular number.")
