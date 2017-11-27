#!/usr/bin/python3
import os
import sys

curr_path = os.path.realpath(__file__)
CHE550_path = curr_path[: curr_path.find('\\', curr_path.find("CHE550"))]
sys.path.append(CHE550_path)

import CHE550_tools

if __name__ == '__main__':

    swissprot_fasta_str, rq_time = CHE550_tools.ut.batch_retrieve_from_uniprot('fasta', reviewed='yes')
    fasta_list = CHE550_tools.ut.uniprot_fasta_parser(swissprot_fasta_str)
    proetin_list = [CHE550_tools.pt.Protein.init_fasta_parse(fasta_str) for fasta_str in fasta_list]

    print(CHE550_tools.DNA.find_dimer_sites())
