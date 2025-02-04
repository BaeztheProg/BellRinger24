word = "This is allowed"
shift_value = 3 
def caesar_cipher(text, shift):
    encodedtext = ''
    for char in text:
        if char.isupper():
            encodedtext += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encodedtext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encodedtext += char
    return encoded_text
encoded_text = caesar_cipher(word, shift_value)
print(encoded_text)
