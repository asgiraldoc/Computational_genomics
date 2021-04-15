import sys
import gzip
import codecs
import io

############### HEADERS ##################

def build_fas_dict(f):                                                                          ### definition of each line as header, footer or sequence
    seq_dict = {}
    for line in f:
        line = line.strip()
        if line.startswith('>'):                                                                ### fasta headers
            header = line
            seq_dict[header] = ''
        elif line.startswith('@'):                                                              ### fastq headers
            header = line
            seq_dict[header] = ''
        elif line.startswith('+'):                                                              ### fastq footers
            header = next(f, '').strip()
            seq_dict[header] = ''
        else:
            seq_dict[header] += line.upper()                                                    ### sequence

    return seq_dict

############### Reverse complement ##############

def reverse_complement(dna_seq):                                                                ### generate the reverse complement of each sequence

    complement = {'A':'T','C':'G','T':'A','G':'C',                                              ### standart nucleotides
    'N':'N','Y':'R','R':'Y',                                                                    ### UPAC nucleotides
    'S':'X','X':'S','W':'Z','Z':'W','K':'M','M':'K','B':'V','D':'H','H':'D','V':'B'}            ### UPAC nucleotides
    rc = "".join(complement.get(base, base) for base in reversed(dna_seq))                      ### reverse complement sequence
    return rc

################# PATTERS ######################
def motifs(dna_seq):                                                                            ### looking for dna motifs on the sequences
    str = 'atgTTG'                                                                              ### interest motif or query
    case = str.upper()
    results = 0
    sub_len = len(case)
    subj = dna_seq                                                                              ### subjetc dna sequence
    for i in range(len(subj)):
        if subj[i:i+sub_len] == case:
            results += 1                                                                        ### count motifs
    return case, results

def Rmotifs(dna_seq):                                                                           ### looking for dna motifs on the sequences
    str = 'atgTTG'                                                                              ### interest motif or query
    Rcase = str.upper()
    Rresults = 0
    sub_len = len(Rcase)
    rc2 = reverse_complement(dna_seq)                                                            ### subjetc reversecomplement sequence
    for i in range(len(rc2)):
        if rc2[i:i+sub_len] == Rcase:                                                           ### count motifs
            Rresults += 1
    return Rcase, Rresults

############### MAIN #####################
filename = sys.argv[1]                                                                          ### input file


if filename.endswith("gz"): 
    a_file = gzip.open(filename, "r")
    read = str(a_file.read(), 'UTF-8')
elif filename.endswith("fastq"):
    a_file = open(filename)
    read = a_file.read()
else:
    a_file = open(filename)
    read = a_file.read()

dna_seq=read
motif = motifs(dna_seq)
Rmotifs = Rmotifs(dna_seq)

print ('The', motif[0], 'is', motif[1], 'times in sequence')
print ('The', Rmotifs[0], 'is', Rmotifs[1], 'times in reverse complement sequence\n')

if len(sys.argv) < 2:
    inf = sys.stdin
elif sys.argv[1].endswith("gz"):
    inf =  io.TextIOWrapper(io.BufferedReader(gzip.open(sys.argv[1])))
else:
    inf =  open(sys.argv[1])
seqs = build_fas_dict(inf)

if inf is not sys.stdin:
    inf.close()

for header, dna_seq in seqs.items():
    rc = reverse_complement(dna_seq)
    print (header)
    count = 0
    while count <= len(rc):
      print (rc[count:count + 101])
      count += 101
