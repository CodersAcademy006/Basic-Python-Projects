import numpy as np

def solve_cubic(a, b, c, d):
    coefficients = [a, b, c, d]
    roots = np.roots(coefficients)
    return roots

# Take input from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = float(input("Enter coefficient d: "))
roots = solve_cubic(a, b, c, d)
print(f"The roots of the cubic equation are {roots}.")
