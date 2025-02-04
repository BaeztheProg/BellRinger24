alphabet = 'abcdefghijklmnopqrstuvwxyz'
capital_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

shift = int(input('What shift do you want for your cipher? (1-26)'))
input_word = input('What word do you want to encode?')
if shift > 25:
    shift = shift % 26
def encode(shift, input_word):
    new_str = ""
    for letter in input_word:
        if letter == ' ':
            new_str += ' '
            print("DANISH")
            continue
        try:
            old_index = alphabet.index(letter)
            new_index = old_index + shift
            if new_index > 25:
                new_index = new_index % 26
            new_str += alphabet[new_index]
        except:
            old_index = capital_alphabet.index(letter)
            new_index = old_index + shift
            if new_index > 25:
                new_index = new_index % 26
            print(new_index)
            new_str += capital_alphabet[new_index]
    print(new_str)
    return new_str
        
final_encoded_string = encode(shift, input_word)
