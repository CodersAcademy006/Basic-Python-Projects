import math

def are_coprime(a, b):
    return math.gcd(a, b) == 1

# Take input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if are_coprime(num1, num2):
    print(f"{num1} and {num2} are co-prime.")
else:
    print(f"{num1} and {num2} are not co-prime.")
