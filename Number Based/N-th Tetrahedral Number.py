def nth_tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 6

# Take input from user
n = int(input("Enter the position of the tetrahedral number: "))
print(f"The {n}-th tetrahedral number is {nth_tetrahedral_number(n)}.")
