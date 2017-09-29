#!/usr/bin/python3


class GOAnnotation(object):

    def __init__(self, go_id, aspect, name):
        self.go_id = go_id
        self.aspect = aspect
        self.name = name

    @classmethod
    def init_parse(cls, annot_str):

        # parse gene ontology identifier
        start_index = annot_str.find('GO:') + 3
        go_id = annot_str[start_index: annot_str.find(';', start_index + 1)]

        # parse aspect
        aspects = {'C': 'Cellular Component', 'F': 'Molecular Function', 'P': 'Biological Process'}
        start_index = annot_str.find(';', start_index + 1) + 2
        aspect = aspects[annot_str[start_index: start_index + 1]]

        # parse name
        name = annot_str[annot_str.find(':', start_index) + 1: annot_str.find(';', start_index + 1)]

        return cls(go_id, aspect, name)
