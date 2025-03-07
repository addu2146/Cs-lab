#Write a program to implement the Playfair cipher for text encryption and decryption.
import numpy as np

def create_matrix(key):
    # Remove duplicates, treat 'J' as 'I'
    key = key.upper().replace('J', 'I')
    seen = set()
    matrix = []

    # Add letters from the key to the matrix
    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    # Add remaining letters of the alphabet to the matrix
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # 'J' is treated as 'I'
    for char in alphabet:
        if char not in seen:
            matrix.append(char)

    # Convert to NumPy array (5x5 matrix)
    matrix = np.array(matrix).reshape(5, 5)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def find_position(matrix, char):
    # Find the position of a character in the 5x5 matrix
    row, col = np.where(matrix == char)
    return row[0], col[0]

def prepare_text(plaintext):
    # Prepare the plaintext by converting to uppercase, replacing 'J' with 'I' and making pairs
    plaintext = plaintext.upper().replace('J', 'I')
    prepared_text = []

    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] != plaintext[i+1]:
            prepared_text.append(plaintext[i] + plaintext[i+1])
            i += 2
        else:
            prepared_text.append(plaintext[i] + 'X')
            i += 1
    
    return prepared_text

def encrypt(text, matrix):
    prepared_text = prepare_text(text)
    encrypted_text = []

    for pair in prepared_text:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])

        if r1 == r2:
            # Same row: Shift columns to the right
            encrypted_text.append(matrix[r1, (c1 + 1) % 5] + matrix[r2, (c2 + 1) % 5])
        elif c1 == c2:
            # Same column: Shift rows down
            encrypted_text.append(matrix[(r1 + 1) % 5, c1] + matrix[(r2 + 1) % 5, c2])
        else:
            # Rectangle: Swap corners
            encrypted_text.append(matrix[r1, c2] + matrix[r2, c1])
    
    return ''.join(encrypted_text)

def decrypt(text, matrix):
    prepared_text = [text[i:i+2] for i in range(0, len(text), 2)]
    decrypted_text = []

    for pair in prepared_text:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])

        if r1 == r2:
            # Same row: Shift columns to the left
            decrypted_text.append(matrix[r1, (c1 - 1) % 5] + matrix[r2, (c2 - 1) % 5])
        elif c1 == c2:
            # Same column: Shift rows up
            decrypted_text.append(matrix[(r1 - 1) % 5, c1] + matrix[(r2 - 1) % 5, c2])
        else:
            # Rectangle: Swap corners
            decrypted_text.append(matrix[r1, c2] + matrix[r2, c1])
    
    return ''.join(decrypted_text)

# Main program to test the Playfair cipher
if __name__ == "__main__":
    key = input("Enter the key for Playfair cipher: ")
    matrix = create_matrix(key)
    print("Playfair cipher key matrix:")
    print_matrix(matrix)

    plaintext = input("Enter the plaintext to encrypt: ")
    encrypted_text = encrypt(plaintext, matrix)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, matrix)
    print(f"Decrypted text: {decrypted_text}")
