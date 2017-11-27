#!/usr/bin/python3
import os
import sys

curr_path = os.path.realpath(__file__)
CHE550_path = curr_path[: curr_path.find('\\', curr_path.find("CHE550"))]
sys.path.append(CHE550_path)

import CHE550_tools

if __name__ == '__main__':
    DNA_seq = input("DNA Sequence (Coding Strand):\n\t")
    DNA_seq_2 = CHE550_tools.DNA.replication(DNA_seq)
    RNA_seq = CHE550_tools.DNA.transcribe(DNA_seq_2)
    pep_seq = CHE550_tools.RNA.translate(RNA_seq)

    print("DNA Seq:")
    print("\t5' " + DNA_seq + " 3'")
    print("\t3' " + DNA_seq_2 + " 5'")

    print("RNA Seq:")
    print("\t5' " + RNA_seq + " 3'")

    print("Polypeptide seq:")
    print("\t" + pep_seq)
