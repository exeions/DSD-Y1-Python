unencrypted_message = input("Input message to encrypt: ")
key = int(input("Input key to use: "))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(message, shift=key):
    encrypted = ""

    for char in message.lower():
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % 26
            encrypted += alphabet[new_index]
        else:
            encrypted += char
    return encrypted

print(encrypt(unencrypted_message))