import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="the input fasta_file")
parser.add_argument("Nvalue", type=int, help="the length of reads")

args = parser.parse_args()

def main():
    fasta = {}
    with open(args.input, "r") as input:
        seq = ""
        for line in input:
            line = line.strip()
            if line[0] == ">":
                fasta[line] = ""
                seq = line
            else:
                if fasta[seq] == "":
                    fasta[seq] = line
                else:
                    fasta[seq] += line
    lengths = [len(x) for x in fasta.values()]
    sort = sorted(lengths, reverse=True)
    assembly = int(sum([len(x) for x in fasta.values()]) * (args.Nvalue/100))
    nvalue = []
    c = 0
    for i in sort:
        c += i
        if c > assembly + i:
            break
        nvalue.append(i)
    print ("The N", args.Nvalue ,"value is", nvalue[-1])


if __name__ == "__main__":
    main()

