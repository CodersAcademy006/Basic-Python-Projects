def count_digits(n):
    return len(str(n))

# Take input from user
num = int(input("Enter a number: "))
print(f"The number of digits in {num} is {count_digits(num)}.")
