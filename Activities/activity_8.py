#!/usr/bin/python3
import os
import sys

curr_path = os.path.realpath(__file__)
CHE550_path = curr_path[: curr_path.find('\\', curr_path.find("CHE550"))]
sys.path.append(CHE550_path)

import CHE550_tools

if __name__ == '__main__':

    # human p53 tumor antigen
    p53_fasta_str, rq_time = CHE550_tools.ut.entry_retrieve_from_uniprot('fasta', 'P04637')
    p53_pro = CHE550_tools.pt.Protein.init_fasta_parse(p53_fasta_str)

    print(p53_pro.id)
    print(p53_pro.accession)
    print(CHE550_tools.pt.amino_acid_to_r_type(p53_pro.sequence))
    CHE550_tools.pt.count_che(CHE550_tools.pt.amino_acid_to_r_type(p53_pro.sequence))
    print()

    # human DNA polymerase theta
    p53_fasta_str, rq_time = CHE550_tools.ut.entry_retrieve_from_uniprot('fasta', 'O75417')
    p53_pro = CHE550_tools.pt.Protein.init_fasta_parse(p53_fasta_str)

    print(p53_pro.id)
    print(p53_pro.accession)
    print(CHE550_tools.pt.amino_acid_to_r_type(p53_pro.sequence))
    CHE550_tools.pt.count_che(CHE550_tools.pt.amino_acid_to_r_type(p53_pro.sequence))
    print()

    # human DNA polymerase theta
    p53_fasta_str, rq_time = CHE550_tools.ut.entry_retrieve_from_uniprot('fasta', 'Q7Z5Q5')
    p53_pro = CHE550_tools.pt.Protein.init_fasta_parse(p53_fasta_str)

    print(p53_pro.id)
    print(p53_pro.accession)
    print(CHE550_tools.pt.amino_acid_to_r_type(p53_pro.sequence))
    CHE550_tools.pt.count_che(CHE550_tools.pt.amino_acid_to_r_type(p53_pro.sequence))
    print()
