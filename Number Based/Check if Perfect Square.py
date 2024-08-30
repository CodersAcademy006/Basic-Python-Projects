import math

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n

# Take input from user
num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(f"{num} is a Perfect Square.")
else:
    print(f"{num} is not a Perfect Square.")
