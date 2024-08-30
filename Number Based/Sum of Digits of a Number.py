# Function to calculate the sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Take input from user
num = int(input("Enter a number: "))
print(f"The sum of the digits of {num} is {sum_of_digits(num)}.")
