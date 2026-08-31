
import binary
import permutation
import padding

def encrypt_text(plain_text,key):
    if len(plain_text)==0 or len(key)==0:
        print("Encryption not possible ")
        return

    plain_text = plain_text.lower()
    print(f"The plain text is {plain_text}\n")

    binary_text = binary.convert_binary(plain_text)
    print(f"The {plain_text} is converted to {binary_text}\n")

    initial_permutation = permutation.initial_permutation_table(binary_text)
    print(f"The result of initial permutation from {binary_text}:{initial_permutation}\n")

    binary_key = binary.convert_binary(key)
    print(f"The key {key}: {binary_key}")
    pad_key = padding.padding_key(binary_key)
    print(f"Padded Key: {pad_key}")

    for block_number, block in enumerate(initial_permutation, start=1):
        L0 = block[:32]
        R0 = block[32:]

        print(f"Block {block_number}")
        print(f"Left:  {L0}")
        print(f"Right: {R0}")

        expanded_R0 = permutation.expansion_permutation(R0)

        print(f"Expanded R0 = {expanded_R0}")
        print(f"Length = {len(expanded_R0)}")

