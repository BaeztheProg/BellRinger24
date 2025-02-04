shift = int(input('What shift do you want for your cipher? (1-26): '))
input_word = input('What word do you want to encode? ')

if shift > 25:
    shift = shift % 26

def encode(shift, input_word):
    new_str = ""
    for letter in input_word:
        if letter == ' ':
            new_str += ' '  
            continue
        
        if 'a' <= letter <= 'z':
            old_index = ord(letter) - ord('a')  
            new_index = (old_index + shift) % 26  
            new_letter = chr(new_index + ord('a'))  
            new_str += new_letter
        
        elif 'A' <= letter <= 'Z':
            old_index = ord(letter) - ord('A') 
            new_index = (old_index + shift) % 26 
            new_letter = chr(new_index + ord('A'))  
            new_str += new_letter
        
    return new_str

final_encoded_string = encode(shift, input_word)
print(f'Encoded word: {final_encoded_string}')
