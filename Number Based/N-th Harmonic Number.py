def nth_harmonic_number(n):
    return sum(1 / i for i in range(1, n + 1))

# Take input from user
n = int(input("Enter the value of n: "))
print(f"The {n}-th Harmonic number is {nth_harmonic_number(n)}.")
