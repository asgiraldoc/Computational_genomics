import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="the input coverage file")
parser.add_argument("output", type=str, help="the output image in png or jpg")

args = parser.parse_args()


def coverage():
    cov = {}
    with open(args.input) as depth_object:
        seq = ""
        for row in depth_object:
            genome_id, depth_count, number_bases, size_genome, fraction = row.split()
            if genome_id.startswith("genome"):
                cov[depth_count] = int(number_bases)
    return cov

def main():
    data  = coverage()
    labels, values = zip(*data.items())
    plt.bar(labels, values, color='#0504aa')
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Number of reads per base position')
    plt.ylabel('Number of base positions')
    plt.savefig(args.output, bbox_inches='tight', dpi=400)
    plt.close()

if __name__ == "__main__":
    main()