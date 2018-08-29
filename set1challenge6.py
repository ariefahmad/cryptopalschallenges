"""
Break repeating-key XOR;
Breaking a Vigenere cipher
"""
import pandas as pd
import base64
import set1challenge3
import set1challenge5
import itertools

def hammingdist_calc(x, y):
    """
    The hamming distance is the number of differing bits (using XOR), with
    the result of XOR-ing 2 bits is 1 ONLY if they are different.
    - bin is used to convert integer to a binary string
    - count is used to.. count number of occurences
    """
    tot_add = 0.
    for i in range(0, len(x)):
        tot_add += bin(x[i] ^ y[i]).count("1")  #XOR then bin & count
    return tot_add

def normalisededit_dist(x):
    """
    Taking 4 keysize blocks then normalising them;
    at the end, sort them by ascending distances
    """
    normalised_dist = []
    for keysize in range(2, 40):
        x1 = x[: keysize]
        x2 = x[keysize: 2 * keysize]
        x3 = x[2 * keysize: 3 * keysize]
        x4 = x[3 * keysize: 4 * keysize]

        normalising = (hammingdist_calc(x1, x2) + hammingdist_calc(x2, x3) + hammingdist_calc(x3, x4)) / (3 * keysize)

        normalised_dist.append((keysize, normalising))

    return sorted(normalised_dist, key=lambda x: x[1])  # want to sort in ascending order of distance

def break_key(x, normalised_dist):
    """
    From challenge:
    Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
    Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
    Solve each block as if it was single-character XOR. You already have code to do this.
    """
    for keysize, _ in normalised_dist[:5]:  # just take first 5 keysizes
        blocks = [x[i: i+keysize] for i in range(0, len(x), keysize)]  # into blocks of keysize length
        transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=0))  # transpose the blocks
        key = [set1challenge3.crack_singlebyteXOR(bytes(x))[0] for x in transposedBlocks]  # solve each block as if it was a single character XOR
        print("Keysize: ", keysize, "\t Extracted key: ", bytes(key))  # extract key
    return 0

if __name__ == '__main__':
    x_test = b"this is a test"
    y_test = b"wokka wokka!!!"

    if hammingdist_calc(x_test, y_test) == 37:
        print("Preliminary test is passed!")

    x = base64.b64decode(open("6.txt", "r").read())

    break_key(x, normalisededit_dist(x))  # get the correct keysize
    # Relevant output:
    # Keysize:  29     Extracted key:  b'Terminator X: Bring the noise'

    break_output = set1challenge5.encode_repkeyXOR(x,  b'Terminator X: Bring the noise')

    print(break_output)
