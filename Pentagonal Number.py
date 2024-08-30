import math

def is_pentagonal(n):
    if n < 1:
        return False
    # Solves the equation k = (sqrt(24*n + 1) + 1) / 6
    k = (math.sqrt(24 * n + 1) + 1) / 6
    return k.is_integer()

# Take input from user
num = int(input("Enter a number: "))
if is_pentagonal(num):
    print(f"{num} is a pentagonal number.")
else:
    print(f"{num} is not a pentagonal number.")
