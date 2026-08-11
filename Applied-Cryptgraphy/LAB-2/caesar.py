def caesar_cipher_encryption(plain_text,key):
    # c = (p+k)mod26
    c =""
    plain_text = plain_text.lower()
    for i in range (len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            ord_num = ord(char) - ord('a')
            temp = (ord_num + key) % 26
            c = c + chr(temp + ord('a'))
        else:
            c = c + char
    return c

def caesar_cipher_decryption(cipher_text,key):
    # p =(c-k)%26
    p = ""
    for i in range (len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            ord_num = ord(char) - ord('a')
            temp = (ord_num - key) % 26
            p = p + chr(temp + ord('a'))
        else:
            p = p + char
    return p

def caesar_cipher():
    plain_text = input("Enter the plain text: ")
    key = int(input("Enter the key: "))
    if(len(plain_text) == 0):
        caesar_cipher()
    encryption = caesar_cipher_encryption(plain_text,key)
    print(f"Encryption of {plain_text} : {encryption}")
    
    cipher_text = input("Enter the cipher text: ")
    key = int(input("Enter the key: "))
    decryption = caesar_cipher_decryption(cipher_text,key)
    print(f"Encryption of {cipher_text} : {decryption}")


caesar_cipher()
