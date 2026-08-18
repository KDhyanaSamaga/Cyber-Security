def brutforce():
    cipher_text = input("Enter the cipher text: ")
    inverse_map = {1: 1,3: 9,5: 21,7: 15,9: 3,11: 19,15: 7,17: 23,19: 11,21: 5,23: 17,25: 25}
    print(f"Ciphertext: {cipher_text}\n")
    print("--- Brute Force Results ---")

    cipher_text = cipher_text.lower()

    for key1,inv_key in inverse_map.items():
        for key2 in range(26):
            plain_text = ""

            for char in cipher_text:
                if char.isalpha():
                    ord_num = ord(char) - ord('a')
                    temp = (inv_key * (ord_num - key2)) % 26
                    plain_text = plain_text + chr(temp + ord('a'))
                else:
                    plain_text = plain_text + char
            print(f"Key a={key1:2d} (Inv={inv_key:2d}), b={key2:2d} -> {plain_text}")
