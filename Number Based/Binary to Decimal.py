def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Take input from user
binary_str = input("Enter a binary number: ")
print(f"The decimal value of binary {binary_str} is {binary_to_decimal(binary_str)}.")
