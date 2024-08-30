import math
# Function to find the GCD of two numbers
def gcd(a, b):
    return math.gcd(a, b)

# Take input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}.")
