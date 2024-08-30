def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Take input from user
num = int(input("Enter a number: "))
print(f"The digital root of {num} is {digital_root(num)}.")
