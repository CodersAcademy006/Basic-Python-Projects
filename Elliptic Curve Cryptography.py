from ecdsa import SECP256k1, SigningKey

def generate_ecc_keys():
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.verifying_key
    return sk, vk

# Key generation
private_key, public_key = generate_ecc_keys()
print("Private Key:", private_key.to_string().hex())
print("Public Key:", public_key.to_string().hex())
