"""
Implement repeating-key XOR;
Encrypting via a Vigenere cipher
"""

import binascii

def encode_repkeyXOR(line, key):
    output = b""  # bytes literal
    for i in range(0, len(line)):
        output += (bytes([line[i] ^ key[i % len(key)]]))  # applying repeating key XOR
    return output

if __name__ == '__main__':
    line_test = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key_test = b"ICE"
    encoded_target = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    encoded_out = binascii.hexlify(encode_repkeyXOR(line_test, key_test)).decode("ascii")  # back to hex & .decode("ascii") for format
    if encoded_out == encoded_target:
        print("Encryption successful!")

    # debugging..
    # for i in range(len(encoded_target)):
    #     if encoded_out[i] != encoded_target[i]:
    #         print("BEANS", i)
