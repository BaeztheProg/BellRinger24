letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
newword = ""

def idk(word):
    global newword
    word = word.lower()
    for i in word:
        if i == " ":
            newword = newword + " "
        else:
            if i in letters:
                new = letters.index(i)
                hi = new + 13
                if hi >= 26:
                    hi = hi - 26
                else:
                    pass
                newword = newword + letters[hi]

    print(newword + "!")

idk("Baez knows")
