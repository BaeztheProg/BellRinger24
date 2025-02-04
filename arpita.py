message = "Baez Knows!"
rot13 = []
for letter in message:
    rot13.append(ord(letter) + 13)
encoded = ""
for point in rot13:
    encoded += chr(point)
print(encoded)
