"""
Implementing PKCS7 padding
"""

def pkcs7_padding(buffer, block_size):
    """
    Append the number of bytes of padding to the end of the block
    """
    ch = block_size - (len(buffer) % block_size)
    return buffer + bytes([ch] * ch)

if __name__ == '__main__':
    buffer_test = b"YELLOW SUBMARINE"
    buffer_out = pkcs7_padding(buffer_test, 20)

    print(buffer_out)
    # Output:
    # b'YELLOW SUBMARINE\x04\x04\x04\x04'
