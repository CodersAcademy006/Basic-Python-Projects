def nth_heptagonal_number(n):
    return n * (5 * n - 3) // 2

# Take input from user
n = int(input("Enter the position of the heptagonal number: "))
print(f"The {n}-th heptagonal number is {nth_heptagonal_number(n)}.")
