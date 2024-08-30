def smallest_digit(n):
    return min(int(digit) for digit in str(n))

# Take input from user
num = int(input("Enter a number: "))
print(f"The smallest digit in {num} is {smallest_digit(num)}.")
