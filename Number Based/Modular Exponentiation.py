def modular_exponentiation(base, exponent, modulus):
    return pow(base, exponent, modulus)

# Take input from user
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
modulus = int(input("Enter the modulus: "))
result = modular_exponentiation(base, exponent, modulus)
print(f"{base}^{exponent} % {modulus} = {result}")
