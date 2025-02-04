string = "Beaz knows!"
shift = int(input("How much should the shift be?"))
encryption = ""
for i in string:
    y=ord(i)
    s=y+shift
    n=chr(s)
    encryption += n
print(encryption)
