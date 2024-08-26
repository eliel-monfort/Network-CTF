def symmetric_encryption(input_data, key):
    # Determine chunk and key size based on length of data (even or odd)
    if len(input_data) % 2 == 0:
        chunk_size = 16
        # Using the all bits of key
        key_in_bits = format(key, '016b')
    else:
        chunk_size = 8
        # Using the last 8 bits of the key
        key_in_bits = format(key, '016b')[-8:]

    # Split data into chunks of appropriate size
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    # Perform XOR operation on each chunk with the key
    result = ""
    for chunk in chunks:
        for bit, key_bit in zip(chunk, key_in_bits):
            result += '1' if bit != key_bit else '0'

    return result


Encrypted_message = '000101111000101100001011100011110000110011000101010100001101000000011011100011010001011010001001000110101101000100011000100100000001000010011000000100111001101001010001100111000001000010010010010100001001101100001101100101100000100110011010010100001001100100010000100100110001101110011010000011011000110001010000110011100001001110101001001101011000101100110110110010110001000010110100000100011011101000100000101111100001010111001110000110001010101100110111110010010011101010101010001100101000110000111101101101100001101110001110001010001011101100010001101101010010111010010011010000001000101000001100100011110100001010001100000101111001111000001101100101100001000110011000'

XorKey = 32767

Decoded_message = symmetric_encryption(Encrypted_message, XorKey)

message = ''.join(chr(int(Decoded_message[i:i + 8], 2)) for i in range(0, len(Decoded_message), 8))

print(message)
