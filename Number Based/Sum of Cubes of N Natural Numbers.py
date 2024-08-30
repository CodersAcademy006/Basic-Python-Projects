def sum_of_cubes(n):
    return (n * (n + 1) // 2) ** 2

# Take input from user
num = int(input("Enter a number: "))
print(f"The sum of cubes of the first {num} natural numbers is {sum_of_cubes(num)}.")
