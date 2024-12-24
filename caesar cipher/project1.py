

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)
while True:
    text = input("Enter Text to encode/decode: ")
    custom_key = input("Enter custom key: ")
    user_choice = input("Enter 'd' to decore, enter 'e' to encode: ").lower()
    print(f'\nText: {text}')
    print(f'Key: {custom_key}')
    if user_choice == "d": 
        decryption = decrypt(text, custom_key)
        print(f'\nDecrypted text: {decryption}\n')
        break
    elif user_choice == "e":
        encryption = encrypt(text, custom_key)
        print(f'\nEncrypted text: {encryption}\n')
        break
    else:
        print("Invalid input, please try again. ")


