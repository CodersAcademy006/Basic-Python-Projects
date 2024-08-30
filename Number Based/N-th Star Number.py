def nth_star_number(n):
    return 6 * n * (n - 1) + 1

# Take input from user
n = int(input("Enter the position of the star number: "))
print(f"The {n}-th star number is {nth_star_number(n)}.")
