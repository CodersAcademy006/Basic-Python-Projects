def is_carmichael(n):
    if n < 2:
        return False
    if any(n % p == 0 for p in range(2, int(n**0.5) + 1) if is_prime(p)):
        return False
    for a in range(2, n):
        if pow(a, n - 1, n) != 1:
            return False
    return True

def carmichael_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if is_carmichael(num)]

# Take input from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Carmichael numbers between {start} and {end} are: {carmichael_numbers_in_range(start, end)}.")
