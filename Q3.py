# This program uses a key to decrypt text that is encrypted by shifting the letters by a "key" number of characters

def decrypt(text, key):
    """This function decrypts encrypted text using a key"""
    
    decrypted_text = "" # declare variables

    for char in text: # iterate through each character
        
        if char.isalpha(): # if character is a letter we  decrypt
            shifted = ord(char) - key # reverse operation to encryption
            
            if char.islower(): # decrypt lowercase letters outside bounds
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26

            elif char.isupper(): # decrypt uppercase letters outside bounds
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)

        else: # if character is not a letter, it does not need to be decrypted
            decrypted_text += char

    return decrypted_text

text = "Guvf grkg jnf rapelcgrq jvgu gur fnzr rapelcgvba hfrq sbe gur 'reebe cebar pbqr'"


#find key with provided code
total = 0
for i in range(5):
    for j in range(3):
        if i + j ==5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter <5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

#print(total)

total = 13 # shift key is 13

print(decrypt(text, total))


#decrypted code from assingment

#global_variable = 100
#
#my_dict = {'key1': 'value1', 'key2': 'vaue2', 'key3': ' value3'}

#def process_numbers():
#	global global_variable
#	global_variable = 5
#	numbers = [1, 2, 3, 4, 5]
#
#	while global_variable > 0:
#		if global_variable %2 == 0:
#		numbers.remove(global_variable) spelling error of remove
#		global_variable -= 1

#	return numbers

#my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
#result =  process_numbers(numbers=my_set)			

#def modify_dict():
#	local_variabe = 10
#	my_dict['key4'] = global_variable 

#modify_dict(5) 

#def update_global():
#	global global_variable
#	global_variable += 10

#for i in range(5):
#	print(i)
#	i += 1

#of my_set is not None and my_dict['key4'] == 10
#	print("Condtion met!")

#if 5 not in my_dict:
#	print("5 not found in the dictionary!")

#print global_variable
#print my_dict
#print myset
###

#fixed code
global_variable = 100

my_dict = {'key1': 'value1', 'key2': 'vaue2', 'key3': ' value3'}

def process_numbers():
	global global_variable
	global_variable = 5
	numbers = [1, 2, 3, 4, 5]

	while global_variable > 0:
		if global_variable % 2 == 0:
		    numbers.remove(global_variable) #spelling error of remove
		global_variable -= 1

	return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result =  process_numbers()			

def modify_dict():
	local_variable = 10
	my_dict['key4'] = global_variable 

modify_dict() #fixed this line wasnt sending anything

def update_global():
	global global_variable
	global_variable += 10

for i in range(5):
	print(i)
	i += 1

if my_set is not None and my_dict['key4'] == 10: # if not of added ":"
	print("Condtion met!")

if 5 not in my_dict:
	print("5 not found in the dictionary!")

print (global_variable) # fixed print commands
print (my_dict)
print (my_set)