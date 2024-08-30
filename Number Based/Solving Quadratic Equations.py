import cmath

def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return root1, root2

# Take input from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
root1, root2 = solve_quadratic(a, b, c)
print(f"The roots of the quadratic equation are {root1} and {root2}.")
