input = "Baez knows"





def caeser(input):
    resut = []
    rot = 13
    
    for letter in input:
        if 'a' <= letter and letter <= 'z':
            resut.append(chr((ord(letter) - ord('a') + rot) % 26 + ord('a')))
        elif 'A' <= letter and letter <= 'Z':
            resut.append(chr((ord(letter) - ord('A') + rot) % 26 + ord('A')))
    
    return resut


input = "Baez knows"
caeser(input)
