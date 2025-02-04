stringy = "Baez Knows!"
units = []
for i in stringy:
    units.append(ord(i)+1)
    for i in units:
        print(chr(i))
