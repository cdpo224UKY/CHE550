#!/usr/bin/python3
"""
This module contains a number of functions to deal with manipulation of DNA sequence data.
"""


def replication(DNA_str):

    DNA_str_2 = str()

    for c in range(0, len(DNA_str)):

        if DNA_str[c] is 'A':
            DNA_str_2 += 'T'

        elif DNA_str[c] is 'C':
            DNA_str_2 += 'G'

        elif DNA_str[c] is 'G':
            DNA_str_2 += 'C'

        elif DNA_str[c] is 'T':
            DNA_str_2 += 'A'

        else:
            print("Invalid character.")
            exit()

    return DNA_str_2


def transcribe(DNA_str):

    RNA_str = str()

    for c in range(0, len(DNA_str)):

        if DNA_str[c] is 'A':
            RNA_str += 'U'

        elif DNA_str[c] is 'C':
            RNA_str += 'G'

        elif DNA_str[c] is 'G':
            RNA_str += 'C'

        elif DNA_str[c] is 'T':
            RNA_str += 'A'

    return RNA_str

