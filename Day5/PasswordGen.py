print("Welcome to the PyPasswordGeneratior!")
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
lettersRange = range(nr_letters)
symbolsRange = range(nr_symbols)
numbersRange = range(nr_numbers)

for letter in lettersRange:
    password += random.choice(letters)
for symbol in symbolsRange:
    password += random.choice(symbols)
for number in numbersRange:
    password += random.choice(numbers)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordList = []

for letter in lettersRange:
    passwordList += random.choice(letters)
for symbol in symbolsRange:
    passwordList += random.choice(symbols)
for number in numbersRange:
    passwordList += random.choice(numbers)

print(passwordList)
random.shuffle(passwordList)

stringPassword = ""
for index in passwordList:
    stringPassword += index

print(f"Your password is : {stringPassword}")