# Function to check if a number is a Neon number
def is_neon(n):
    square_sum = sum(int(digit) for digit in str(n * n))
    return n == square_sum
# Take input from user
num = int(input("Enter a number: "))
if is_neon(num):
    print(f"{num} is a Neon number.")
else:
    print(f"{num} is not a Neon number.")
