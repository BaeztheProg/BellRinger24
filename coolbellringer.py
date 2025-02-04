message = "baez knows!"
message.lower().strip()
key = 13
ans = ""
englishAns = ""
letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for char in message: 
    if char == " ":
        pass
    elif char == "!":
        englishAns += '!'
    elif char == 'z':
        englishAns += 'a'
    else:
        addOn = ord(char) + key
        #print(addOn)
        ans += chr(addOn)

        englishAns += letters[letters.index(char) + 1]

print(ans)
print(englishAns)
