"""
Detect single-character XOR
"""

import set1challenge3
import pandas as pd

if __name__ == '__main__':
    reader = pd.read_csv("4.txt", delimiter=" ", header=None)
    for lines in range(0, len(reader[0])):
        print("Line: ", lines)
        print(set1challenge3.crack_singlebyteXOR(bytes.fromhex(reader[0][lines])))

# Output:
# Line:  170
# (53, 2.3613299999999993, b'Now that the party is jumping\n')

    print(set1challenge3.crack_singlebyteXOR(bytes.fromhex(reader[0][170]))[2].decode("ascii"))  # final formatting
