
def padding_to_binary(binary_text):

    binary_text = "".join(binary_text.split())

    chunk_size = 64
    all_blocks = []

    for i in range(0, len(binary_text), chunk_size):
        chunk = binary_text[i : i + chunk_size]

        if len(chunk) < chunk_size:
            chunk = chunk + "1" + "0" * (chunk_size - len(chunk) - 1)

        block_ints = list(map(int, list(chunk)))
        all_blocks.append(block_ints)

    return all_blocks

def padding_key(binary_key):
    binary_key = "".join(binary_key.split())
    chunk_size = 64

    if len(binary_key) < chunk_size:
            binary_key = binary_key + "0" * (chunk_size - len(binary_key))
            
    elif len(binary_key) > chunk_size:
            binary_key = binary_key[:chunk_size]

    return [int(b) for b in binary_key]

