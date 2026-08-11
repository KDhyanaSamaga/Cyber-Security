def get_key_inverse(key):
    if key<1:
        exit()
    else:
        key_inverse = None
        for i in range(1,26):
            if(key*i)%26==1:
                key_inverse = i
                break
    return key_inverse

def multiplicative_cipher_decryption(cipher_text,key):
    plain_text = ""
    inverse_key = get_key_inverse(key)
    cipher_text = cipher_text.lower()

    for char in cipher_text:
        if char.isalpha():
            ord_num = ord(char) - ord('a')
            temp = (ord_num*inverse_key)%26
            plain_text = plain_text + chr(temp + ord('a'))
        else:
            plain_text = plain_text + char

    return plain_text


def multiplicative_cipher_encryption(plain_text,key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            ord_num = ord(char) - ord('a')
            temp = (ord_num*key)%26
            cipher_text = cipher_text + chr(temp + ord('a'))
        else:
            cipher_text = cipher_text + char  

    return cipher_text

def multiplicative_cipher():
    plain_text = input("Enter the plain text: ")
    key = int(input("Enter the key: "))

    encryption = multiplicative_cipher_encryption(plain_text,key)
    print(f"Encryption of {plain_text} : {encryption}")

    cipher_text = input("Enter the cipher text: ")
    key1 = int(input("Enter the key: "))
    decryption = multiplicative_cipher_decryption(cipher_text,key1)
    print(f"Decryption of {cipher_text} : {decryption}")

multiplicative_cipher()