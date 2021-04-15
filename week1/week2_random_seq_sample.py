import random

def rand_seq_start_stop(seqlength,readlength):
    start = random.randint(0,seqlength-readlength-1)
    return start, start + readlength

## when using a random number generater it is usually best to
## set the seed for each run
## requires a positive integer
# random.seed(7)

bases ='ACGT'
seqlength = 1000
readlength = 100
## make a list of seqlength random bases
seqlist = [random.choice(bases) for i in range(seqlength)]
## join up the individual bases into a string to make the sequence
seq = ''.join(seqlist)
print(seq)

numreads = 5
for i in range(numreads):
    pos= rand_seq_start_stop(seqlength,readlength)
    print(pos, seq[pos[0]:pos[1]])
