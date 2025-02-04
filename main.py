def textencrypter():
    encryptedtxt = input("Enter Text to encrypt: ")
    
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    encryptedversion = ""

    for char in encryptedtxt:
        if char in lowercase:  
            i = lowercase.index(char)
            i = (i + 13) % 26  #decided to use the % for remainder over going back to starting from 0-26 again 
            encryptedversion += lowercase[i]
        elif char in uppercase: 
            i = uppercase.index(char)
            i = (i + 13) % 26
            encryptedversion += uppercase[i]
        else:
            encryptedversion += char 

    return encryptedversion

print(textencrypter())
