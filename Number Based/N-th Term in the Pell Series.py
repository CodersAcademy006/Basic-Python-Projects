def pell_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, 2 * b + a
    return b

# Take input from user
n = int(input("Enter the position in the Pell series: "))
print(f"The {n}-th Pell number is {pell_number(n)}.")
