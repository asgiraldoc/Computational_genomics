
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

estseq = "TTCTTAATGTCCCTAGCCATTGCTGATATGCTAGTGGGACTACTTGTCATGCCACTGTCTCTGCTTGCAATCCTTTATGATTATGTCTGGCCACTACCTAGATATTTGTGCCCCGTCTGGATTTCTTTAGATGTTTTATTTTCTACAGCGTCCATCATGCACCTCTGCGCTATTTCGCTGGATCGGTATGTAGCAGTACGTAATCCATGTGAGCATAGCCGTTGCAATTCACGGACAAAGGCCATCATGAAGATTGC"

blast_result_handle = NCBIWWW.qblast(program="blastx",database="refseq_protein",sequence= estseq,entrez_query= "txid9606[ORGN]")

blast_records = NCBIXML.parse(blast_result_handle)

## look at the first record
blast_record = next(blast_records)
print ("# alignments:",len(blast_record.alignments))
for alignment in blast_record.alignments[0:1]:
    print ("hit_id:",alignment.hit_id)
    print ("hit_def:",alignment.hit_def)

blast_result_handle.close()



