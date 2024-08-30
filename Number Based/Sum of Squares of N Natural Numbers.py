def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

# Take input from user
num = int(input("Enter a number: "))
print(f"The sum of squares of the first {num} natural numbers is {sum_of_squares(num)}.")
