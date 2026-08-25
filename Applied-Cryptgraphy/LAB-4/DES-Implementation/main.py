import encrypt

def main():
    print("DES Algorithm Implementation")
    plain_text = input("Enter the plain text:")

    print(f"The entered plain text is {plain_text}")
    key = input(f"Enter the key to encrypt {plain_text}:")
    
    result = encrypt.encrypt_text(plain_text,key)
    print(f"The plain text {plain_text} + {key} = {result}")

if __name__ == "__main__":
    main()
