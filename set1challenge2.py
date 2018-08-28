"""
Function that takes two equal-length buffers and produces their
exclusive OR gate (XOR) combination
"""

import binascii
import base64

def fixed_XOR(hex_valA, hex_valB):
    xor_d = int(hex_valA, 16) ^ int(hex_valB, 16)  # cast string (hex) to int values then apply XOR operator
    return format(xor_d, "x")  # format back to hex

if __name__ == '__main__':
    encodedA = "1c0111001f010100061a024b53535009181c"
    encodedB = "686974207468652062756c6c277320657965"
    hex_target = "746865206b696420646f6e277420706c6179"

    if fixed_XOR2(encodedA, encodedB) == hex_target:
        print("XOR'd!")
