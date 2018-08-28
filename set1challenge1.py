"""
Convert hex to base64
"""

import binascii
import base64

def hex_to_base64(hex_var):
    decoded = binascii.unhexlify(hex_var)
    return base64.b64encode(decoded).decode("ascii")

if __name__ == '__main__':
    hex_test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base64_target = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    if hex_to_base64(hex_test) == base64_target:
        print("Conversion successful!")
