def playFair_cipher_encryption(plain_text,key):
    cipher_text = ""
    plain_text = plain_text.lower()
    key = key.lower()

    matrix = []
    for char in key:
        matrix.append(char)

def playFair_cipher():
    plain_text = input("Enter the plain text: ")
    key = input("Enter the key: ")

    encryption = playFair_cipher_encryption(plain_text,key)

