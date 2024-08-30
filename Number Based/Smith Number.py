def is_smith_number(n):
    def prime_factors(x):
        factors = []
        for i in range(2, int(x**0.5) + 1):
            while x % i == 0:
                factors.append(i)
                x //= i
        if x > 1:
            factors.append(x)
        return factors

    def sum_of_digits(x):
        return sum(int(digit) for digit in str(x))

    factors = prime_factors(n)
    return sum_of_digits(n) > sum_of_digits(sum(factors)) and len(factors) > 1

# Take input from user
num = int(input("Enter a number: "))
if is_smith_number(num):
    print(f"{num} is a Smith number.")
else:
    print(f"{num} is not a Smith number.")
