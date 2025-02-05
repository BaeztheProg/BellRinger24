letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
newword = ""

def idk(word):
    for i in word:
        if i in letters:
            new = letters.index(i)
            hi = new + 13
            newword.append(letters[hi])

    print(newword)

print(idk("hi"))
