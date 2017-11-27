#!/usr/bin/python3
import os
import sys

curr_path = os.path.realpath(__file__)
CHE550_path = curr_path[: curr_path.find('\\', curr_path.find("CHE550"))]
sys.path.append(CHE550_path)

import CHE550_tools

if __name__ == '__main__':
    membrane_pro_str, rq_time = CHE550_tools.ut.batch_retrieve_from_uniprot('txt', reviewed='yes', keyword='812')
    membrane_pro_list = CHE550_tools.ut.uniport_txt_parser(membrane_pro_str)

    membrane_proteins = list()
    for membrane_pro in membrane_pro_list:
        membrane_proteins.append(CHE550_tools.pt.Protein.init_txt_parse(membrane_pro))


    helix_pro_str, rq_time = CHE550_tools.ut.batch_retrieve_from_uniprot('txt', reviewed='yes', keyword='1133')
    helix_pro_list = CHE550_tools.ut.uniport_txt_parser(helix_pro_str)

    helix_proteins = list()
    for helix_pro in helix_pro_list:
        helix_proteins.append(CHE550_tools.pt.Protein.init_txt_parse(helix_pro))


    sheet_pro_str, rq_time = CHE550_tools.ut.batch_retrieve_from_uniprot('txt', reviewed='yes', keyword='1134')
    sheet_pro_list = CHE550_tools.ut.uniport_txt_parser(sheet_pro_str)

    sheet_proteins = list()
    for sheet_pro in sheet_pro_list:
        sheet_proteins.append(CHE550_tools.pt.Protein.init_txt_parse(sheet_pro))

    print(len(membrane_proteins))
    print(len(helix_proteins))
    print(len(sheet_proteins))
