"""
Implementing CBC mode
"""

import base64
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

class CBC_mode:
    """docstring for ."""
    def __init__(self, ECB, IV):
        """
        txt in plaintext
        """
        self.ECB = ECB
        self.IV = IV
        self.block_size = 16

    def cbc_encrypt(self, plaintext):
        n_blocks = [plaintext[i: i + self.block_size] for i in range(0, len(plaintext), self.block_size)]
        ciphertext = b""
        prev_block = self.IV
        for i in range(0, len(n_blocks)):
            curr_block = n_blocks[i]
            ciph_block = self.ECB.encrypt(strxor(curr_block, prev_block))
            ciphertext += ciph_block
            prev_block = ciph_block  # update
        return ciphertext

    def cbc_decrypt(self, ciphertext):
        n_blocks = [ciphertext[i: i + self.block_size] for i in range(0, len(ciphertext), self.block_size)]
        plaintext = b""
        prev_block = self.IV
        for i in range(0, len(n_blocks)):
            curr_block = n_blocks[i]
            plai_block = strxor(self.ECB.decrypt(curr_block), prev_block)
            plaintext += plai_block
            prev_block = curr_block
        return plaintext

if __name__ == '__main__':
    plaintext = base64.b64decode(open("10.txt", "r").read())
    key = b"YELLOW SUBMARINE"

    cipher = CBC_mode(AES.new(key, AES.MODE_ECB), bytes([0] * 16))
    dec_plaintext = cipher.cbc_decrypt(plaintext)
    enc_back = cipher.cbc_encrypt(dec_plaintext)

    if enc_back == plaintext:
        print("Decrypt & re-encrypt successful!")
