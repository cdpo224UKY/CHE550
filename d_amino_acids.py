#!/usr/bin/python3
import CHE550_tools

d_amino_acids, rq_time = CHE550_tools.ut.retrieve_from_uniprot('txt', reviewed='yes', keyword='208')
d_amino_acids_list = CHE550_tools.ut.uniport_txt_parser(d_amino_acids)

peptides = list()
for d_amino_acid in d_amino_acids_list:
    peptides.append(CHE550_tools.pt.Protein.init_parse(d_amino_acid))

print(peptides[0].annotations[0].go_id)

functions = list()
for pep in peptides:
    for annot in pep.annotations:
        functions.append(annot.go_id)

unique_annotations = sorted(set(functions), key=functions.count)

print("Number peptides: " + str(len(d_amino_acids_list)))
print("Number of functions: " + str(len(functions)))
print("Number of unique functions: " + str(len(set(functions))))

print("Top 5 functions:")
print("\tRank Term      Num ")
print("\t1.   GO:" + str(unique_annotations[-1]) + " " + str(functions.count(unique_annotations[-1])))
print("\t2.   GO:" + str(unique_annotations[-2]) + " " + str(functions.count(unique_annotations[-2])))
print("\t3.   GO:" + str(unique_annotations[-3]) + " " + str(functions.count(unique_annotations[-3])))
print("\t4.   GO:" + str(unique_annotations[-4]) + " " + str(functions.count(unique_annotations[-4])))
print("\t5.   GO:" + str(unique_annotations[-5]) + " " + str(functions.count(unique_annotations[-5])))
