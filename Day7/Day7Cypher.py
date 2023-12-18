alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt ( text, shift) -> str:
    modifiedText = ""
    for letter in text:
        position = alphabet.index(letter)
        new_Position = position + shift
        if new_Position > len(alphabet):
            new_Position = new_Position - len(alphabet)
        newLetter = alphabet[new_Position]
        modifiedText += newLetter
    return modifiedText

def decrypt (text, shift) -> str:
    return encrypt(text, -shift)

if direction == "encode" :
    print(encrypt(text, shift))
elif direction == "decode" :
    print(decrypt(text, shift))
# else:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")