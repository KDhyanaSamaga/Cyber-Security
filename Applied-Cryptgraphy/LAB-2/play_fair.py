import numpy as np

def playFair_cipher_encryption(plain_text,key):
    cipher_text = ""
    plain_text = plain_text.lower()
    key = key.lower()

    matrix = []
    for char in key:
        matrix.append(char)

    # Remove J Since we dont use that much
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in matrix:
        if char not in matrix:
            matrix.append(char)

    matrix = np.array(matrix).reshape(5,5)
    



def playFair_cipher():
    plain_text = input("Enter the plain text: ")
    key = input("Enter the key: ")

    encryption = playFair_cipher_encryption(plain_text,key)

