# Function to check if a number is even or odd
def is_even_or_odd(n):
    return "even" if n % 2 == 0 else "odd"

# Take input from user
num = int(input("Enter a number: "))
result = is_even_or_odd(num)
print(f"{num} is {result}.")
