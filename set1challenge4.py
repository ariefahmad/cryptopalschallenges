"""
Detect single-character XOR
"""

import set1challenge3
import pandas as pd

reader = pd.read_csv("4.txt", delimiter=" ", header=None)
print((reader[0][325]))

for lines in range(0, len(reader[0])):
    print("Line: ", lines)
    print(set1challenge3.crack_singlebyteXOR(reader[0][lines]))

# Output:
# Line:  170
# (53, 2.3613299999999993, b'Now that the party is jumping\n')
