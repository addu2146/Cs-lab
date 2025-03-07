# Function to encrypt text using Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97  # ASCII value for A and a
            encrypted_text += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters are added unchanged
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift) 

# Main program to interact with the user
if __name__ == "__main__":
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    # Encrypt the text
    encrypted_text = caesar_encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")
    
    # Decrypt the text back
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")
