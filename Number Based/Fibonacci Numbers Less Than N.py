def fibonacci_less_than(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# Take input from user
num = int(input("Enter the upper limit for Fibonacci numbers: "))
print(f"Fibonacci numbers less than {num} are: {fibonacci_less_than(num)}.")
