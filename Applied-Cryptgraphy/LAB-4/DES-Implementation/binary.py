
def convert_binary(plain_text):
    binary = []

    for char in plain_text:
        ascii_val = ord(char)
        
        binary_val = format(ascii_val, '08b')
        binary.append(binary_val)  
        
    return ' '.join(binary)
