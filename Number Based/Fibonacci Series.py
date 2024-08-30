# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series

# Take input from user
num = int(input("Enter the number of terms in the Fibonacci series: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The Fibonacci series with {num} terms is: {fibonacci(num)}.")
