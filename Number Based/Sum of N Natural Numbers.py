# Function to calculate the sum of the first N natural numbers
def sum_natural_numbers(n):
    return n * (n + 1) // 2

# Take input from user
num = int(input("Enter a number: "))
print(f"The sum of the first {num} natural numbers is {sum_natural_numbers(num)}.")
