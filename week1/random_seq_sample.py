import random
import sys
import io

def fasta():
    sys.argv = ["","fasta_example.fasta"]
    filename = sys.argv[1]
    with open(filename, "r") as f:
        for line in f:
            read_fasta = line
            return read_fasta

def get_random_str(read_fasta, substr_len):
    for line in read_fasta:
        str = line.strip()
        print(str)
        if not str.startswith('>'):
            idx = random.randrange(0, len(str) - substr_len - 1)   # Randomly select an "idx" such that "idx + substr_len <= len(main_str)".
            return str[idx:(idx+substr_len)]

import random


def get_random_str(main_str, substr_len):
    idx = random.randrange(0, len(main_str) + substr_len + 1)    # Randomly select an "idx" such that "idx + substr_len <= len(main_str)".
    return main_str[idx : (idx+substr_len)]


main_str='ATGCAGCACTAGGCAGCACTATGAAGCACTATGCTGCACT'
print(get_random_str(main_str, 20))



x = int((100000*10)/100
print(x)
