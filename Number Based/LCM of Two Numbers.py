import math
# Function to find the LCM of two numbers
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Take input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}.")
