
# Secret Code Language
# This program allows you to encode (encrypt) and decode (decrypt) a message
# using a Caesar cipher technique, where each letter is shifted by a number chosen by the user.
# Example: with shift=2, 'a' -> 'c', 'y' -> 'a'.

def encode(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                # Shift within lowercase letters
                encoded_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                # Shift within uppercase letters
                encoded_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encoded_message += char
    return encoded_message

def decode(message, shift):
    decoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                # Reverse shift within lowercase letters
                decoded_message += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                # Reverse shift within uppercase letters
                decoded_message += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decoded_message += char
    return decoded_message

# Ask the user to enter a message
input_message = input("Enter your message: ")

# Ask the user whether they want to encode (encrypt) or decode (decrypt)
action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()  

# Ask the user for the shift value
shift_value = int(input("Enter the shift value (number of positions to move): "))

# Based on user input, call the appropriate function
if action == 'encode':
    print("Encoded message:", encode(input_message, shift_value))
elif action == 'decode':
    print("Decoded message:", decode(input_message, shift_value))