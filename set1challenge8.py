"""
Detect AES in ECB mode
"""

def detectAES(textfile):
    data = open(textfile, "r").read()
    lines = data.split("\n")
    line_num = 0
    current_max = 0
    for line in lines:
        blocks = [line[i: i+16] for i in range(0, len(line), 16)] # into blocks of 16 bytes
        similar_cnt = 0
        for fb in blocks:  # loop over first block
            for sb in blocks:  # loop over second block
                if fb == sb:
                    similar_cnt += 1
        if similar_cnt > current_max:  # get line with most similar counts
            current_max = similar_cnt
            probable_line = line_num
        line_num += 1
    return lines[probable_line]

if __name__ == '__main__':

    print(detectAES("8.txt"))
    # Output:
    # d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a
