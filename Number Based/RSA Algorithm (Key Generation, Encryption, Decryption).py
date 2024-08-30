import random
from sympy import isprime, mod_inverse

def generate_keypair(bits=1024):
    p = q = 1
    while not isprime(p):
        p = random.getrandbits(bits // 2)
    while not isprime(q) or q == p:
        q = random.getrandbits(bits // 2)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))  # Public and private keys

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Key generation
public_key, private_key = generate_keypair()

# Encryption
plaintext = input("Enter the message to encrypt: ")
ciphertext = encrypt(public_key, plaintext)
print("Encrypted message:", ciphertext)

# Decryption
decrypted_message = decrypt(private_key, ciphertext)
print("Decrypted message:", decrypted_message)
