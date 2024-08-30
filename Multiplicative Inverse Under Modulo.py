def multiplicative_inverse(a, m):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (g, x, y)

    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Multiplicative inverse does not exist')
    return x % m

# Take input from user
a = int(input("Enter the number: "))
m = int(input("Enter the modulus: "))
inverse = multiplicative_inverse(a, m)
print(f"The multiplicative inverse of {a} mod {m} is {inverse}.")
