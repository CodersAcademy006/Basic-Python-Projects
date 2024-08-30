def lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    a, b = 2, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# Take input from user
n = int(input("Enter the position in the Lucas series: "))
print(f"The {n}-th Lucas number is {lucas_number(n)}.")
