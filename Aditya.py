inp = input("What you like to encode:\n")

msg = []
for letter in inp:
    msg.append(letter)

encoded_msg = ""
for each in msg:
    msg = ord(each)
    msg += 15
    msg = chr(msg)
    encoded_msg += msg

print(encoded_msg)
