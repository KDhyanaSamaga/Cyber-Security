def brutforce():
    cipher_text = input("Enter the cipher text: ")
    print(f"Ciphertext: {cipher_text}\n")
    print("--- Brute Force Results ---")

    cipher_text = cipher_text.lower()

    for key in range(26):
        plain_text = ""
        for char in cipher_text:
            if char.isalpha():
                ord_num = ord(char) - ord('a')
                decrypted_char = (ord_num - key) % 26
                plain_text = plain_text + chr(decrypted_char + ord('a'))
            else:
                plain_text = plain_text + char

        print(f"Key {key:2d} -> {plain_text}")
