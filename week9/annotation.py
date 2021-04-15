import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_pep", type=str, help="pep file")
parser.add_argument("input_pfam", type=str, help="pfam file")
parser.add_argument("input_blastP", type=str, help="blastP file")
parser.add_argument("output", type=str, help="output file")

args = parser.parse_args()

def hmms():
    
    with open(args.input_pfam) as g:
        f = g.readlines()
        t = reversed(f)
        hmms_dic = {}
        for row in t:
            if not row.startswith("#"):
                rows = " "
                row_complete = row.split(maxsplit=4)
                z = row_complete[0:4]           
                x = rows.join(z)
                domain_name,accession,tlen,query = x.split()
                hmms_dic[query] = domain_name
    return hmms_dic

def blasP():
    blasP_dic = {}
    with open(args.input_blastP, "r") as f:
        for line in f:
            if line.startswith("Query= "):
                x = line.strip()
                nn, query, type, len = x.split(maxsplit=3)
                next(f)
                next(f)
                next(f)
                next(f)
                next(f)
                next(f)
                next(f)
                next(f)
                best_hint = next(f)
                id_and_name = best_hint[:-30]
                blasP_dic[query] = id_and_name
    return blasP_dic

def pep():
    pep_dic = {}
    with open(args.input_pep, "r") as f:
        for line in f:
            if line.startswith(">"):                
                header=line.replace(">","")
                query, stuff = header.split(maxsplit=1)
                seq_pep = next(f)
                len_pep = str(len(seq_pep[:-1]))
                l_pep = "  ----  " + len_pep
                pep_dic[query] = l_pep
    return pep_dic

def main():
    pfam_DB = hmms()
    ncbi_DB = blasP()
    transcritps = pep()
    pep_pfam = {key: transcritps[key] + "  ----  " + pfam_DB.get(key, '') for key in transcritps.keys()} 
    result = {key: pep_pfam[key] + "  ----  " + ncbi_DB.get(key, '') for key in pep_pfam.keys()} 
    f = open(args.output,'w')
    print ("(1) Sequence ID, (2) Length, (3) best match of Pfam domain, (4)  best match of blastp ID and name",file=f )   
    for i,j in result.items():
        print(i, j, file=f)
    f.close()

if __name__ == "__main__":
    main()

