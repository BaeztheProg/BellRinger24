def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_char = char  
        
        encrypted_text += encrypted_char
    
    return encrypted_text
#Exakmple
plaintext = "Hello, World!"
shift_value = 3  
encrypted = caesar_cipher(plaintext, shift_value)
print(f"Encrypted Text: {encrypted}")
