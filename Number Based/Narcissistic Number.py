def is_narcissistic(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

# Take input from user
num = int(input("Enter a number: "))
if is_narcissistic(num):
    print(f"{num} is a Narcissistic number.")
else:
    print(f"{num} is not a Narcissistic number.")
