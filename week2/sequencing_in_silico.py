import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="the input fasta_file")
parser.add_argument("output", type=str, help="the output fastq_file")
parser.add_argument("readlenght", type=int,
                    help="the length of reads")
parser.add_argument("depth", type=int,
                    help="desired in silico sequencing depth")
args = parser.parse_args()

def main():
    gsize = 100000 ## genome size
    numreads = int((gsize*args.depth)/args.readlenght)
    with open(args.output, "w") as output: # open output file fastq
        with open(args.input, "r") as input: #  Open and read fasta file
            for line in input:      #       extract substring from fasta file
                seqlength = ''.join(line.strip() for line in input)
                i = 0
                for i in range(numreads):
                    i += 1
                    fa2fq = line.replace(">","@" + str(i))
                    output.write("\n" + fa2fq )     #write sequences ID
                    idx = random.randint(0, len(seqlength)-args.readlenght-1) # Randomly select a read
                    output.write(seqlength[idx:(idx+args.readlenght)]) #write --> substring
                    output.write("\n+\n") # write + (format fq file)
                    output.write(str("I"*args.readlenght))   # write quality


if __name__ == "__main__":
    main()
#Project started 2013-01-03
