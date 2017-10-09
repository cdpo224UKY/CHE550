#!/usr/bin/python3
import CHE550_tools

amino_acid_r_group_chemistry = {
    'G': 'n', 'A': 'n', 'P': 'n', 'V': 'n',
    'L': 'n', 'I': 'n', 'M': 'n',

    'F': 'a', 'Y': 'a', 'W': 'a',

    'S': 'u', 'C': 'u', 'T': 'u', 'N': 'u',
    'Q': 'u',

    'K': '+', 'H': '+', 'R': '+',

    'D': '-', 'E': '-'
}


def amino_acid_to_r_type(pro_str):

    r_group_che_str = str()

    for x in range(0, len(pro_str)):
        r_group_che_str += amino_acid_r_group_chemistry[pro_str[x]]

    return r_group_che_str


def count_che(pro_str):

    n_count = pro_str.count('n')
    a_count = pro_str.count('a')
    u_count = pro_str.count('u')
    p_count = pro_str.count('+')
    e_count = pro_str.count('-')

    print('n: ' + str(n_count) + " %: " + str(n_count/len(pro_str)))
    print('a: ' + str(a_count) + " %: " + str(a_count/len(pro_str)))
    print('u: ' + str(u_count) + " %: " + str(u_count/len(pro_str)))
    print('+: ' + str(p_count) + " %: " + str(p_count/len(pro_str)))
    print('-: ' + str(e_count) + " %: " + str(e_count/len(pro_str)))


class Protein(object):

    def __init__(self, id, accession, seq, annot):
        self.id = id
        self.accession = accession
        self.sequence = seq
        self.annotations = annot

    @classmethod
    def init_txt_parse(cls, entry_str):

        # parse id
        start_index = entry_str.find('ID   ') + 5
        id = entry_str[start_index: entry_str.find(' ', start_index + 1)]

        # parse accession
        start_index = entry_str.find('AC   ') + 5
        accession = entry_str[start_index: entry_str.find(';', start_index)]

        # parse annotation(s)
        start_index = entry_str.find('DR   GO')
        annots = list()

        while start_index != -1:
            annot = CHE550_tools.got.GOAnnotation.init_parse(entry_str[start_index: entry_str.find('\n', start_index)])
            annots.append(annot)

            start_index = entry_str.find('DR   GO', start_index + 1)

        # parse seq
        seq = 'ABC'

        return cls(id, accession, seq, annots)

    @classmethod
    def init_fasta_parse(cls, fasta_str):

        ac_s = fasta_str.find('|') + 1
        ac_e = fasta_str.find('|', ac_s + 1)

        accession = fasta_str[ac_s: ac_e]
        id = fasta_str[ac_e + 1: fasta_str.find(' ') + 1]
        seq = fasta_str[fasta_str.find('\n'):].replace('\n', '')

        return cls(id, accession, seq, None)

    def __len__(self):
        return len(self.sequence)
