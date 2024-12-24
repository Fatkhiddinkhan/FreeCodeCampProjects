# Caesar Cipher Encoder/Decoder

Welcome to the **Caesar Cipher Encoder/Decoder** project, part of my [FreeCodeCamp Scientific Computing with Python](https://www.freecodecamp.org/) journey!

## Project Overview

In this project, I implemented the classic **Caesar Cipher** technique to encode and decode messages. This exercise helped me solidify my understanding of Python functions and fundamental programming concepts.

## What is a Caesar Cipher?

The Caesar Cipher is a simple encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3:

- **Plaintext**: HELLO
- **Ciphertext**: KHOOR

## Features

- **Encode Messages**: Shift letters forward in the alphabet to encrypt messages.
- **Decode Messages**: Shift letters backward to decrypt messages.
- **Custom Shift**: Choose any integer value as the shift number. Positive numbers for encoding and negative numbers for decoding.
- **Preserve Case**: Maintains the case of the original message.
- **Handle Non-alphabet Characters**: Leaves spaces, numbers, and symbols unchanged to ensure message integrity.

## How It Works

1. **Input Message**: Provide the message you want to encode or decode.
2. **Shift Number**: Enter a text shift value.
   - **Shifting Number**: Encodes/Decodes the message by length of letter given.
3. **Output**: Receive the safely encoded or decoded message.

## Example Usage

### Encoding a Message

```python
message = "Hello, World!"
shift = "mike"
direction = 'e' ("in forward direction")
decryption = decrypt(text, custom_key)
print(encoded_message)  # Outputs: Khoor, Zruog!