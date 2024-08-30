def largest_digit(n):
    return max(int(digit) for digit in str(n))

# Take input from user
num = int(input("Enter a number: "))
print(f"The largest digit in {num} is {largest_digit(num)}.")
