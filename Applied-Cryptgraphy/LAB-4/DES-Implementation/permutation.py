import padding

def initial_permutation_table(binary_text):
    initial_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

    padded_binary = padding.padding_to_binary(binary_text)
    print(f"The padded binary are : {padded_binary}\n")
    permuted_blocks = []

    for block in padded_binary:
        permuted_block = [block[i - 1] for i in initial_table]
        permuted_blocks.append(permuted_block)

    return permuted_blocks


def expansion_permutation(right_half):
    expansion_table = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]

    expanded_block = []
    for i in expansion_table:
        bit = right_half[i - 1]
        expanded_block.append(bit)

    return expanded_block
