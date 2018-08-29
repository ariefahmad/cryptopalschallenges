"""
Cracking a single byte XOR cipher; known as Caesar cipher
"""

import binascii

# getting character frequencies from
# http://www.sxlist.com/techref/method/compress/etxtfreq.htm
freqs = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074,
    ' ': 0.19182
}

def score_sys(char):
    """
    Scoring system for a piece of English plaintext;
    just sum the character frequency for each character
    """
    tot_score = 0
    for i in char:
        char = chr(i).lower()
        if char in freqs:
            tot_score += freqs[char]
    return tot_score

def XOR_singlechar(str, key):
    """
    Performs XOR logic between a byte array & an integer
    """
    output = b""  # bytes literal
    for char in str:
        output += bytes([char ^ key])  # applying XOR
    return output

def crack_singlebyteXOR(cipher_bytes):
    """
    Cracking the cipher; cipher_bytes in bytes
    """
    candidates = list()
    for key_candidate in range(256):
        byte_candidate = XOR_singlechar(cipher_bytes, key_candidate)
        candidates.append((key_candidate, score_sys(byte_candidate), byte_candidate))
    return max(candidates, key=lambda x: x[1])  # sort by max in score array

if __name__ == '__main__':
    encodedA = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    decodedA = bytes.fromhex(encodedA)
    print(crack_singlebyteXOR(decodedA)[2].decode("ascii"))

# Output:
# (88, 2.5316499999999995, b"Cooking MC's like a pound of bacon")
