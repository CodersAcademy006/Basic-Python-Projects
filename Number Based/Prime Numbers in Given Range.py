# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find prime numbers in a range
def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

# Take input from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers between {start} and {end} are: {primes_in_range(start, end)}.")
