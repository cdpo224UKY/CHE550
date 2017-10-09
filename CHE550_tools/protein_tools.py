#!/usr/bin/python3
import CHE550_tools


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
        seq = fasta_str[fasta_str.find('\n'):]

        return cls(id, accession, seq, None)

    def __len__(self):
        return len(self.sequence)
