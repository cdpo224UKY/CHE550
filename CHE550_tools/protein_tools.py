#!/usr/bin/python3
import CHE550_tools


class Protein(object):

    def __init__(self, id, accession, seq, annot):
        self.id = id
        self.accession = accession
        self.sequence = seq
        self.annotations = annot

    @classmethod
    def init_parse(cls, entry_str):

        # parse id
        start_index = entry_str.find('ID   ') + 5
        id = entry_str[start_index: entry_str.find(' ', start_index + 1)]

        # parse accession
        start_index = entry_str.find('AC   ') + 5
        accession = entry_str[start_index: entry_str.find(';', start_index)]

        # parse annotation(s)
        start_index = entry_str.find('DR   ')
        annot = CHE550_tools.got.GOAnnotation.init_parse(entry_str[start_index: entry_str.find('\n', start_index)])

        seq = 'ABC'

        return cls(id, accession, seq, annot)

    def __len__(self):
        return len(self.sequence)
