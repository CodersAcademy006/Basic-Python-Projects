def nth_hexagonal_number(n):
    return n * (2 * n - 1)

# Take input from user
n = int(input("Enter the position of the hexagonal number: "))
print(f"The {n}-th hexagonal number is {nth_hexagonal_number(n)}.")
