# this is caeser cipher decoder

from colorama import Fore, init

init()

def caeser_cipher(text, key, decrypt=False):
	result = " "
	
	for char in text:
		if char.isalpha():
			shift = key if not decrypt else -key
			if char.islower():
				result += chr(((ord(char) - ord('a') + shift) %26) + ord('a'))
			else:
				result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
		else:
			result += char
	return result
	
def crack_caeser_cipher(ciphertext):
	for key in range(26):
		decrypt_text = caeser_cipher(ciphertext, key, decrypt=True)
		print(f"Key - {key}: {decrypt_text}")

while True:
	encrypted_text = input(f"please enter the text for decrypt: ")
	
	if not encrypted_text:
		print('please specify the text to decrypt')
	else:
	 	crack_caeser_cipher(encrypted_text)