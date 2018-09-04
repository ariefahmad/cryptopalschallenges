"""
An ECB/CBC detection oracle
"""

import base64
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from Crypto.Random import random
import set2challenge10
import set2challenge9
from random import randint

def random_keybytes(length):
    return random.getrandbits(6*length).to_bytes(length, byteorder="big")

def encryption_oracle(buffer):
    rand_key = random_keybytes(16)
    cipher = AES.new(rand_key, AES.MODE_ECB)


    if randint(0, 1) == 0:  # 50% chance
        print("Applying ECB encryption")
        ECB_switch = 0
    else:
        print("Applying CBC encryption")
        IV = random_keybytes(16)
        cipher = set2challenge10.CBC_mode(cipher, IV)
        ECB_switch = 1

    buffer = random_keybytes(randint(5, 10)) + buffer + random_keybytes(randint(5, 10))
    buffer = set2challenge9.pkcs7_padding(buffer, 16)

    if ECB_switch == 0:
        return cipher.encrypt(buffer)
    if ECB_switch == 1:
        return cipher.cbc_encrypt(buffer)

def method_detector(encryption_oracle):
    buffer = bytes([0] * 47)
    test = encryption_oracle(buffer)
    if test[16:32] == test[32:48]:
        return "ECB"
    return "CBC"

if __name__ == '__main__':
    print(method_detector(encryption_oracle))
