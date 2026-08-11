def affine_cipher_decryption(cipher_text, key1, key2):
    plain_text = ""
    cipher_text = cipher_text.lower()
    
    for char in cipher_text:
        if char.isalpha():
            char_ord_num = ord(char) - ord('a')
            temp = (key1 * (char_ord_num - key2)) % 26
            plain_text += chr(temp + ord('a'))
        else:
            plain_text += char
            
    return plain_text

def affine_cipher_encryption(plain_text,key1,key2):
    cipher_text = ""
    plain_text = plain_text.lower()
    for char in plain_text:
        if char.isalpha():
            char_ord_num = ord(char) - ord('a')
            temp = ((key1*char_ord_num)+key2)%26
            cipher_text = cipher_text + chr(temp + ord('a'))
        else:
            cipher_text = cipher_text + char

    return cipher_text

def affine_cipher():
    plain_text = input("Enter the plain text: ")
    key1 = int(input("Enter the first key: "))
    key2 = int(input("Enter the second key: "))

    encryption = affine_cipher_encryption(plain_text,key1,key2)
    print(f"Encryption of {plain_text} : {encryption}")

    cipher_text = input("Enter the cipher text: ")
    key1 = int(input("Enter the key1 inverse: "))
    key2 = int(input("Enter the second key2: "))

    decryption = affine_cipher_decryption(cipher_text,key1,key2)
    print(f"Decryption of {cipher_text} : {decryption}")

affine_cipher()
