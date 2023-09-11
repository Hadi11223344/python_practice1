def caesar_cipher(text, shift):
    encrypted_text = ''
    
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            if char.islower():  # Check if the character is lowercase
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char  # Keep non-alphabetic characters unchanged
        
        encrypted_text += encrypted_char

    return encrypted_text

# Get user input
phrase = input("Enter sentence to encrypt: ")
shift = int(input("Enter shift value: "))

# Encrypt the phrase
encoded_phrase = caesar_cipher(phrase, shift)

# Print the result
print("The encoded phrase is:", encoded_phrase)
