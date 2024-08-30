def nth_nonagonal_number(n):
    return n * (7 * n - 6) // 2

# Take input from user
n = int(input("Enter the position of the nonagonal number: "))
print(f"The {n}-th nonagonal number is {nth_nonagonal_number(n)}.")
