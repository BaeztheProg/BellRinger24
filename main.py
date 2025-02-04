text = 'Baez Knows'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

def encrypt(text, shift):
  new_text = ''
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      if new_position > 25:
        new_position = new_position - 26
      new_text += alphabet[new_position]
    else:
      new_text += char
  return new_text

print(encrypt(text, 13))
