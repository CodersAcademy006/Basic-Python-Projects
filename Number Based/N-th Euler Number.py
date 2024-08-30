from sympy import euler

def nth_euler_number(n):
    return euler(n)

# Take input from user
n = int(input("Enter the position of the Euler number: "))
print(f"The {n}-th Euler number is {nth_euler_number(n)}.")
