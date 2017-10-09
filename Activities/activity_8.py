#!/usr/bin/python3
import os
import sys

curr_path = os.path.realpath(__file__)
CHE550_path = curr_path[: curr_path.find('\\', curr_path.find("CHE550"))]
sys.path.append(CHE550_path)

import CHE550_tools

if __name__ == '__main__':
    p53_fasta_str, rq_time = CHE550_tools.ut.entry_retrieve_from_uniprot('fasta', 'P04637')
    print(p53_fasta_str)
    p53_pro = CHE550_tools.pt.Protein.init_fasta_parse(p53_fasta_str)
    print(p53_pro.id)
    print(p53_pro.accession)
    print(str(p53_pro.sequence))
