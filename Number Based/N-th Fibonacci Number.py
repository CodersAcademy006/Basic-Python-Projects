def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Take input from user
n = int(input("Enter the position of the Fibonacci number to find: "))
print(f"The {n}-th Fibonacci number is {fibonacci(n)}.")
