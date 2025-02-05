input1 = input("Enter a Text: ")
shift = input("Shift by how Much: ")
output = []
for each in input1:
    temp = ord(each)
    temp += int(shift)
    output.append(chr(temp))
print(output)
