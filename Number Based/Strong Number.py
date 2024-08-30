import math
# Function to check if a number is a Strong number
def is_strong(n):
    def factorial(x):
        return 1 if x == 0 else x * factorial(x - 1)
    
    return n == sum(factorial(int(digit)) for digit in str(n))

# Take input from user
num = int(input("Enter a number: "))
if is_strong(num):
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")
