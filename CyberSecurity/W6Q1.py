def xor_encrypt_decrypt(plaintext, key):
    # XOR each character with the key
    result = ''.join(chr(ord(c) ^ key) for c in plaintext)
    return result

plaintext = "Cyber Security"

# Keys 
keys = [0, 1, 5]

# Perform encryption and decryption 
for key in keys:
    print(f"\nUsing XOR key: {key}")
    
    # Encryption
    encrypted_text = xor_encrypt_decrypt(plaintext, key)
    print(f"Encrypted text: {(encrypted_text)}")
    
    # Decryption 
    decrypted_text = xor_encrypt_decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")
