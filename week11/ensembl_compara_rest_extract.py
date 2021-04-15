"""
@author: dliberles
modified by JH  4/5/2019
"""

import requests, sys;

base_url = "http://rest.ensembl.org";

#extract gene ids from file into list
gene_file = open("mart_export_gibbon.txt");
##numgenes = 100
numgenes = 2
gene_list = [];
rownum = 0
for line in gene_file:
    if rownum > 0:
        gene_list.append(line.split()[0])
    rownum += 1
    if rownum > numgenes:
        break
gene_file.close()

trees = [];
homologs = [];
for i in range(len(gene_list)):
    query = base_url+"/genetree/member/id/"+gene_list[i]+"?"+"compara=multi;nh_format=simple";
    print (query)
    tree=requests.get(query, headers={ "Content-Type" : "text/x-nh"});
    trees.append(tree.text);
##    print (i,tree.text)
    query_homologs = base_url+"/homology/id/"+gene_list[i]+"?"+"format=condensed;type=orthologues";
    homolog= requests.get(query_homologs, headers={ "Content-Type" : "text/xml"});
    homologs.append(homolog.text);

print(trees, homologs);
