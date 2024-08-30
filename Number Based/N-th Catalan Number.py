import math

def catalan_number(n):
    return math.comb(2 * n, n) // (n + 1)

# Take input from user
n = int(input("Enter the position of the Catalan number: "))
print(f"The {n}-th Catalan number is {catalan_number(n)}.")
