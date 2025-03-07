import string

# Helper function to convert text to numbers and numbers to text
def text_to_numbers(text):
    alphabet = string.ascii_uppercase
    text = text.upper().replace(' ', '')  # Remove spaces and convert to uppercase
    return [alphabet.index(char) for char in text]

def numbers_to_text(numbers):
    alphabet = string.ascii_uppercase
    return ''.join([alphabet[num] for num in numbers])

# Simple Feistel Round Function (XOR-based)
def round_function(right_half, round_key):
    #  the round function is just an XOR with the round key
    return [(x ^ round_key) % 26 for x in right_half]

# Feistel Cipher Encryption
def feistel_encrypt(plaintext, key, rounds=4):
    # Convert the plaintext to numbers
    numbers = text_to_numbers(plaintext)
    
    # Split the text into two halves (left and right)
    half_len = len(numbers) // 2
    left_half = numbers[:half_len]
    right_half = numbers[half_len:]
    
    # Apply Feistel rounds
    for round_num in range(rounds):
        round_key = key[round_num % len(key)]  # Round key rotates through the key
        # Apply the round function to the right half, XOR with the left half
        new_left = [(l ^ round_key) % 26 for l in right_half]  # XOR left half with round key
        new_right = left_half
        left_half, right_half = new_left, new_right
    
    # Combine left and right halves
    ciphertext = left_half + right_half
    return numbers_to_text(ciphertext)

# Feistel Cipher Decryption (reverse the Feistel rounds)
def feistel_decrypt(ciphertext, key, rounds=4):
    # Convert the ciphertext to numbers
    numbers = text_to_numbers(ciphertext)
    
    # Split the text into two halves (left and right)
    half_len = len(numbers) // 2
    left_half = numbers[:half_len]
    right_half = numbers[half_len:]
    
    # Apply Feistel rounds in reverse order
    for round_num in range(rounds-1, -1, -1):
        round_key = key[round_num % len(key)]  # Round key rotates through the key
        # Apply the round function to the left half, XOR with the right half
        new_right = [(r ^ round_key) % 26 for r in left_half]  # XOR right half with round key
        new_left = right_half
        left_half, right_half = new_left, new_right
    
    # Combine left and right halves
    plaintext = left_half + right_half
    return numbers_to_text(plaintext)

# Main program to encrypt and decrypt using the Feistel Cipher
if __name__ == "__main__":
    # Define a simple key (list of numbers for round keys)
    key = [3, 12, 7, 18]  # Example round keys
    
    # Input plaintext
    plaintext = "HELLO WORLD"
    
    print(f"Original plaintext: {plaintext}")
    
    # Encrypt the plaintext
    ciphertext = feistel_encrypt(plaintext, key)
    print(f"Encrypted ciphertext: {ciphertext}")
    
    # Decrypt the ciphertext
    decrypted_text = feistel_decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")
