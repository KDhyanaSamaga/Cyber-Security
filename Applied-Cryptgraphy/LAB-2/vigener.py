def vigener_cipher_encryption(plain_text,key):
    cipher_text = ""
    key_index = 0
    plain_text = plain_text.lower()
    key = key.lower()

    for char in plain_text:
        if char.isalpha():
            char_ord_num = ord(char) - ord('a')
            key_ord_num = ord(key[key_index]) - ord('a')

            temp = (char_ord_num + key_ord_num) % 26
            cipher_text += chr(temp + ord('a'))
            key_index = key_index+1
            if(key_index >= len(key)):
                key_index = 0
        else:
            cipher_text += char
    return cipher_text

def vigener_cipher_decryption(cipher_text,key):
    plain_text = ""
    key_index = 0
    cipher_text = cipher_text.lower()
    key = key.lower()

    for char in cipher_text:
        if char.isalpha():
            char_ord_num = ord(char) - ord('a')
            key_ord_num = ord(key[key_index]) - ord('a')

            temp = (char_ord_num - key_ord_num) % 26
            plain_text = plain_text + chr(temp + ord('a'))
            key_index = key_index + 1
            if(key_index >= len(key)):
                key_index = 0
        else:
            plain_text = plain_text + char

    return plain_text

def vigener_cipher():
    plain_text = input("Enter the plain text: ")
    key = input("Enter the key: ")
    if(len(plain_text) == 0):
        vigener_cipher()
    encryption = vigener_cipher_encryption(plain_text,key)
    print(f"Encryption of {plain_text} : {encryption}")
        
    cipher_text = input("Enter the cipher text: ")
    key = input("Enter the key: ")
    decryption = vigener_cipher_decryption(cipher_text,key)
    print(f"Encryption of {cipher_text} : {decryption}")


vigener_cipher()
