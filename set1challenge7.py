"""
AES in ECB mode; decrypting a ciphertext
"""

import base64
from Crypto.Cipher import AES

if __name__ == '__main__':
    x = base64.b64decode(open("7.txt", "r").read())  # cipher text; encrypted using AES-128 (meaning blocks are 128 bits long)
    key = b"YELLOW SUBMARINE"
    cipher = AES.new(key, AES.MODE_ECB)
    x_cipherd = cipher.decrypt(x)
    print(x_cipherd)
