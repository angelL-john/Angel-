# This program finds the ASCII values of the uppercase letters and even numbers of a string

s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

# declare variables
numbers = ""
letters = ""
ASCII_numbers = []
ASCII_letters = []

# split characters and numbers
for char in s:
    if char.isalpha():
        letters += char
    else:
        numbers += char

# test prints
# print(numbers)
# print(letters)


# Find uppercase letters and append into ASCII decimal value
for char in letters:
    if char.isupper():
        ASCII_letters.append(ord(char))

# Find even number and append them to ASCII decimal value
for char in numbers:
    if int(char) % 2 == 0:
        ASCII_numbers.append(ord(char))

print(ASCII_numbers)
print(ASCII_letters)