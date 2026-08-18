def frequency(cipher_text:str):
    freq = {}
    cipher_text = cipher_text.lower()
    for char in cipher_text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    return freq

def analyze():
    cipher_text = input("Enter the cipher text: ")
    char_count = frequency(cipher_text)
    char_count = sorted(char_count.items())
    print(f"Ciphertext: {cipher_text}\n")
    print("--- Character Frequencies (High to Low) ---")
    for char, count in char_count:
        print(f"'{char}': {count} time(s)")
