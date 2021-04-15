import random


def main():
    barcodes = ['ATGAGATCTT', 'AGCTCATTTC', 'TGAAAATCTT', 'TATCCAGCCA', 'AGGCAGGCAG',
                'CTTGTTACTA', 'AAGGCACAAG', 'TGCTCGCTGA', 'GTACCGCCGT', 'CCTCACCAGC']

    for i in barcodes:
        with open(i + ".txt", "w") as outputs:                              ##Write files named for each barcode
            with open("week3_seqs.fq", "r") as input:
                while True:
                    line = input.readline()                                 ##read first line
                    if len(line) == 0:          
                        break    
                    sline = input.readline()                                ##read second line          
                    newsline = random.choice(barcodes) + sline[10:]         ##randomly choose a barcode and concatenate it with the second line 
                    nobar = newsline[10:]                                   ##remove the barcode
                    sum = input.readline()                                  ##read third line 
                    quality = input.readline()                              ##read fourth line 
                    noqual = quality[10:]                                   ##remove the first 10 letters coding quality
                    if i == i:                                              ##if the bardode is equal to itself
                        if newsline.startswith(i):                          ##if the newline starts with the same barcode as the previous conditional do the following
                            outputs.write(line)                             ##write the output files
                            outputs.write(nobar)
                            outputs.write(sum)
                            outputs.write(noqual)

if __name__ == "__main__":
    main()