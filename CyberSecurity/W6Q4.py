import numpy as np
import string

def text_to_numbers(text):
    alphabet = string.ascii_uppercase
    text = text.upper().replace(' ', '')  
    return [alphabet.index(char) for char in text]

def numbers_to_text(numbers):
    alphabet = string.ascii_uppercase
    return ''.join([alphabet[num] for num in numbers])

# Hill Cipher Encryption
def encrypt(plaintext, key_matrix):
    numbers = text_to_numbers(plaintext)
    
    # Make sure the length is even, adding 'X' (0) if necessary
    if len(numbers) % 2 != 0:
        numbers.append(0)  # Add 'A' (0) if odd length
    
    # Reshape numbers into pairs of 2x1 vectors
    numbers = np.array(numbers).reshape(-1, 2).T  # Shape into 2 rows (vectors of 2 elements)
    
    # Encrypt using matrix multiplication (mod 26)
    ciphertext = np.dot(key_matrix, numbers) % 26
    ciphertext = ciphertext.T.flatten()  # Flatten the result back into a 1D array
    
    return numbers_to_text(ciphertext)

# Hill Cipher Decryption (using NumPy)
def decrypt(ciphertext, key_matrix):
    # Inverse of the matrix (mod 26)
    det = int(np.linalg.det(key_matrix))  # Get determinant of the key matrix
    det_inv = pow(det, -1, 26)  # Modular inverse of the determinant
    key_matrix_inv = det_inv * np.round(np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)).astype(int) % 26  # Inverse mod 26
    
    # Convert ciphertext to numbers
    numbers = text_to_numbers(ciphertext)
    
    # Reshape numbers into pairs of 2x1 vectors
    numbers = np.array(numbers).reshape(-1, 2).T  # Shape into 2 rows (vectors of 2 elements)
    
    # Decrypt using matrix multiplication (mod 26)
    plaintext = np.dot(key_matrix_inv, numbers) % 26
    plaintext = plaintext.T.flatten()  # Flatten the result back into a 1D array
    
    return numbers_to_text(plaintext)

# Main program to encrypt and decrypt a text file
if __name__ == "__main__":
    # Define the Hill Cipher 2x2 key matrix
    key_matrix = np.array([[6, 24], [1, 16]])  # Example matrix (invertible modulo 26)
    
    # Read the plaintext file
    with open("plaintext.txt", "r") as file:
        plaintext = file.read()
    
    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key_matrix)
    print(f"Encrypted ciphertext: {ciphertext}")
    
    # Save the encrypted text to a file
    with open("ciphertext.txt", "w") as file:
        file.write(ciphertext)
    
    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext, key_matrix)
    print(f"Decrypted text: {decrypted_text}")
    
    # Save the decrypted text to a file
    with open("decrypted.txt", "w") as file:
        file.write(decrypted_text)

