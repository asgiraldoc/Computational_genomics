import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="genes.fpkm_tracking file")
parser.add_argument("output", type=str, help="the output image in png or jpg")

args = parser.parse_args()

def fpkm():
    fpkm_value = {}
    with open(args.input) as FPKM:
        for row in FPKM:
            tracking_id,class_code,nearest_ref_id,gene_id,gene_short_name,tss_id,locus,length,coverage,FPKM,FPKM_conf_lo,FPKM_conf_hi,FPKM_status = row.split()
            if not gene_id.startswith("gene_id"):
                fpkm_value[gene_id] = float(FPKM)
    return fpkm_value

def main():
    data  = fpkm()
    labels = data.values()
    bins= [0,0.00000001,0.0000001,0.000001 ,0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000]
    plt.hist(labels, bins, edgecolor="k")
    plt.xscale('log')
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('FPKM')
    plt.ylabel('Numbers of genes')
    plt.savefig(args.output, bbox_inches='tight', dpi=400)
    plt.close()


if __name__ == "__main__":
    main()