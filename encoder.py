# caeser cipher encode uchun dastur yozamiz 1-qism (satomoru) (darknet_off1cial)

import os, sys

from colorama import Fore, init

init()

def caeser_cipher(message, key, decrypt=False):
	
	result = " "
	
	for character in message:
		if character.isalpha():
			shift = key if  not decrypt else -key
			if character.islower():
				result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
			else:
				result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
		
		else:
			result += character
		
	return result

text_to_encrypt = input(f'Please enter your text message for encode: ')
key = int(input(f'please specify the shift length: '))

if key > 26 or key < 0:
	print(f'your shift length should be between 0 and 26')
	sys.exit()

encrypted_text = caeser_cipher(text_to_encrypt, key)

print(f'has been encrypted as: {encrypted_text}')