#!/usr/bin/python3
"""
This module contains a number of functions to deal with manipulation of DNA sequence data.
"""
RNA_codons = {
    'UUU': 'Phe',   'UCU': 'Ser',   'UAU': 'Tyr',   'UGU': 'Cys',
    'UUC': 'Phe',   'UCC': 'Ser',   'UAC': 'Tyr',   'UGC': 'Cys',
    'UUA': 'Leu',   'UCA': 'Ser',   'UAA': 'Stop',  'UGA': 'Stop',
    'UUG': 'Leu',   'UCG': 'Ser',   'UAG': 'Stop',  'UGG': 'Trp',

    'CUU': 'Leu',   'CCU': 'Pro',   'CAU': 'His',   'CGU': 'Arg',
    'CUC': 'Leu',   'CCC': 'Pro',   'CAC': 'His',   'CGC': 'Arg',
    'CUA': 'Leu',   'CCA': 'Pro',   'CAA': 'Gln',   'CGA': 'Arg',
    'CUG': 'Leu',   'CCG': 'Pro',   'CAG': 'Gln',   'CGG': 'Arg',

    'AUU': 'Ile',   'ACU': 'Thr',   'AAU': 'Asn',   'AGU': 'Ser',
    'AUC': 'Ile',   'ACC': 'Thr',   'AAC': 'Asn',   'AGC': 'Ser',
    'AUA': 'Ile',   'ACA': 'Thr',   'AAA': 'Lys',   'AGA': 'Arg',
    'AUG': 'Met',   'ACG': 'Thr',   'AAG': 'Lys',   'AGG': 'Arg',

    'GUU': 'Val',   'GCU': 'Ala',   'GAU': 'Asp',   'GGU': 'Gly',
    'GUC': 'Val',   'GCC': 'Ala',   'GAC': 'Asp',   'GGC': 'Gly',
    'GUA': 'Val',   'GCA': 'Ala',   'GAA': 'Glu',   'GGA': 'Gly',
    'GUG': 'Val',   'GCG': 'Ala',   'GAG': 'Glu',   'GGG': 'Gly',
}

letter_symbol = {
    'Ala': 'A',
    'Cys': 'C',
    'Asp': 'D',
    'Glu': 'E',
    'Phe': 'F',
    'Gly': 'G',
    'His': 'H',
    'Ile': 'I',
    'Lys': 'K',
    'Leu': 'L',
    'Met': 'M',
    'Asn': 'N',
    'Pro': 'P',
    'Pyl': 'O',
    'Gln': 'Q',
    'Arg': 'R',
    'Ser': 'S',
    'Sec': 'U',
    'Thr': 'T',
    'Val': 'V',
    'Trp': 'W',
    'Tyr': 'Y',
}


def translate(RNA_str):

    pep_str = str()
    count = 0

    while count <= (len(RNA_str) - 3):

        if RNA_codons[RNA_str[count: count + 3]] is 'Stop':
            return pep_str

        else:
            pep_str += letter_symbol[RNA_codons[RNA_str[count: count + 3]]]
            count += 3

    return pep_str
