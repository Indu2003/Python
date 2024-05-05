def CustomCaesarCipher(key, message):
    if key < 0:
        return "INVALID INPUT"

    cipher_text = ""
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.isdigit():  # Check if the character is a digit
            shifted_char = chr((ord(char) - ord('0') + key) % 10 + ord('0'))
        else:
            shifted_char = char  # Keep non-alphabetic and non-numeric characters unchanged
        cipher_text += shifted_char

    return cipher_text


# Example usage
plain_text = input("Enter your PlainText: ")
key = int(input("Enter the Key: "))
encrypted_text = CustomCaesarCipher(key, plain_text)
print("\nThe encrypted Text is:", encrypted_text)
