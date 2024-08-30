def chinese_remainder_theorem(a, n):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (g, x, y)

    def mod_inv(a, m):
        g, x, _ = extended_gcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        return x % m

    x = 0
    prod = 1
    for ni in n:
        prod *= ni

    for ai, ni in zip(a, n):
        p = prod // ni
        x += ai * mod_inv(p, ni) * p
    return x % prod

# Take input from user
a = [int(x) for x in input("Enter the remainders separated by spaces: ").split()]
n = [int(x) for x in input("Enter the moduli separated by spaces: ").split()]
result = chinese_remainder_theorem(a, n)
print(f"The solution to the Chinese Remainder Theorem is {result}.")
