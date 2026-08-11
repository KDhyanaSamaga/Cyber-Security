# 1. Caesar cipher

**File Name**:**caesar.py**

### Code

```python
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
```

### Output

<img src="photo/caesar.png" width="600" height="300" alt="Resized Image">

---

# 2.Vigener Cipher

**File Name** : vigener.py

### Code

```python
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
```

### Output

<img src="photo/vigener.png" width="600" height="300" alt="Resized Image">

---

# 3.Affine Cipher

**File Name : affine.py**

### Code

```python
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
```

### Output

<img src="photo/affine.png" width="600" height="300" alt="Resized Image">

---

# 4.Hill Cipher

### Code

```python
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


hill_cipher()
```

### Output

<img src="photo/affine.png" width="600" height="300" alt="Resized Image">

---

# 5.Multiplicative Cipher

**File Name : multiplicative.py**

```python
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
```

### Output

<img src="photo/affine.png" width="600" height="300" alt="Resized Image">

---

# 6.Play Fair Cipher

**File Name : play_fair.py**

```python

```

### Output

<img src="photo/affine.png" width="600" height="300" alt="Resized Image">

---
