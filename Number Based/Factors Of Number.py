# Function to find factors of a number
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Take input from user
num = int(input("Enter a number: "))
print(f"The factors of {num} are: {factors(num)}.")
