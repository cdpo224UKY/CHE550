#!/usr/bin/python3
import CHE550_tools

d_amino_acids, rq_time = CHE550_tools.ut.retrieve_from_uniprot('txt', reviewed='yes', keyword='208')
d_amino_acids_list = CHE550_tools.ut.uniport_txt_parser(d_amino_acids)

print(len(d_amino_acids_list))

testy = CHE550_tools.pt.Protein.init_parse(d_amino_acids_list[0])

print(testy.id)
print(testy.accession)
print(testy.annotations.name)
