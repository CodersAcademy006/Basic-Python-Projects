def is_disarium(n):
    num_str = str(n)
    return n == sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))

# Take input from user
num = int(input("Enter a number: "))
if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")
