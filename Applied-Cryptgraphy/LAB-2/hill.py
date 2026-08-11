import numpy as np
from sympy import  Matrix

def hill_cipher_decryption(cipher_text,key):
    det = int(np.linalg.det(key))
    key = Matrix(key)
    adj_key = key.adjugate() #inbuilt function for adjoint of the matrix else loop through 
    det_inverse = pow(det,-1,26)
    new_key = (det_inverse * adj_key)

    for i in range(new_key.rows):
        for j in range(new_key.cols):
            if new_key[i,j]<0:
                new_key[i,j] = new_key[i,j]+26

    new_key = new_key.tolist()
    decryption = hill_cipher_encryption(
        cipher_text,
        new_key,
        len(new_key)
    )
    decryption = decryption.replace('x',"")

    return decryption


def hill_cipher_encryption(plain_text,key,size):
   
    if len(plain_text)%size == 0:
        pass
    else:
        while len(plain_text) % size != 0:
            plain_text += 'X'

    plain_text = plain_text.lower()
    cipher_text = ""

    ord_list = []
    for char in plain_text:
        if char.isalpha():
            num_value = ord(char) - ord('a')
            ord_list.append(num_value)

    for i in range(0,len(ord_list),size):
        plain_vector = ord_list[i : i + size]
        
        for r in range(size):
            total = 0
            for c in range(size):
                total += key[r][c] * plain_vector[c]
                
            cipher_text += chr((total % 26) + ord('a'))

    return cipher_text


def hill_cipher():
    plain_text = input("Enter the plain text: ")
    row = int(input("Size of row"))
    column = int(input("SIze of column"))
    if(row!=column):
        print("THE ROW AND COLUMN MUST BE SAME IN HILL CIPHER")
        hill_cipher()

    key = []
    for i in range(row):
        c = []
        for j in range(column):
            c.append(int(input()))
        key.append(c)

    print(f"Key : {key}")
    encryption = hill_cipher_encryption(plain_text,key,row)
    print(f"Encryption of {plain_text} : {encryption}")

    cipher_text = input("Enter the cipher text: ")
    row1 = int(input("Size of row"))
    column1 = int(input("SIze of column"))
    if(row1 != column1):
        print("THE ROW AND COLUMN MUST BE SAME IN HILL CIPHER")
        hill_cipher()

    key1 = []
    for i in range(row1):
        c = []
        for j in range(column1):
            c.append(int(input()))
        key1.append(c)
    decryption = hill_cipher_decryption(cipher_text,key1)
    print(f"Encryption of {cipher_text} : {decryption}")

hill_cipher()
