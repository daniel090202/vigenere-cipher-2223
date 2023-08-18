def generate_key(original_text, key):
	key = list(key)

	if len(key) >= len(original_text):
		return(key)
	else:
		for i in range(len(original_text) - len(key)):
			key.append(key[i % len(key)])

	return("" . join(key))
	
def get_cipher_text(original_text, key):
	cipher_text = []

	for i in range(len(original_text)):
		x = (ord(original_text[i]) + ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))

	return("" . join(cipher_text))
	
def get_original_text(cipher_text, key):
	original_text = []

	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
		x += ord('A')
		original_text.append(chr(x))

	return("" . join(original_text))

if __name__ == "__main__":
	print("Press 1: Encryption")
	print("Press 2: Decryption")

	number = input("Your choice: ")

	if(number == "1"):
		original_text = input("Your input: ")
		keyword = input("Your keyword: ")

		key = generate_key(original_text, keyword)
		cipher_text = get_cipher_text(original_text,key)

		print("Decryption: ", cipher_text)
	elif(number == "2"):
		cipher_text = input("Your input: ")
		keyword = input("Your keyword: ")

		key = generate_key(cipher_text, keyword)
		original_text = get_original_text(cipher_text,key)

		print("Decryption: ", original_text)
	


	

