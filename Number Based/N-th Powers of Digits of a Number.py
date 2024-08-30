def sum_of_nth_powers_of_digits(n, power):
    return sum(int(digit) ** power for digit in str(n))

# Take input from user
num = int(input("Enter a number: "))
power = int(input("Enter the power: "))
print(f"The sum of the digits of {num} each raised to the power of {power} is {sum_of_nth_powers_of_digits(num, power)}.")
