# Function to check if a number is perfect
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# Take input from user
num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
