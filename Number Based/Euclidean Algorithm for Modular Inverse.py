def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Take input from user
a = int(input("Enter the number: "))
m = int(input("Enter the modulus: "))
inverse = modular_inverse(a, m)
print(f"The modular inverse of {a} mod {m} is {inverse}")
