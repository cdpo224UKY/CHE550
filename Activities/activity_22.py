#!/usr/bin/python3
import os
import sys

curr_path = os.path.realpath(__file__)
CHE550_path = curr_path[: curr_path.find('\\', curr_path.find("CHE550"))]
sys.path.append(CHE550_path)

identifiers = [
    ">1 dna:chromosome chromosome:GRCh38:1:1:248956422:1 REF",
    ">10 dna:chromosome chromosome:GRCh38:10:1:133797422:1 REF",
    ">11 dna:chromosome chromosome:GRCh38:11:1:135086622:1 REF",
    ">12 dna:chromosome chromosome:GRCh38:12:1:133275309:1 REF",
    ">13 dna:chromosome chromosome:GRCh38:13:1:114364328:1 REF",
    ">14 dna:chromosome chromosome:GRCh38:14:1:107043718:1 REF",
    ">15 dna:chromosome chromosome:GRCh38:15:1:101991189:1 REF",
    ">16 dna:chromosome chromosome:GRCh38:16:1:90338345:1 REF",
    ">17 dna:chromosome chromosome:GRCh38:17:1:83257441:1 REF",
    ">18 dna:chromosome chromosome:GRCh38:18:1:80373285:1 REF",
    ">19 dna:chromosome chromosome:GRCh38:19:1:58617616:1 REF",
    ">2 dna:chromosome chromosome:GRCh38:2:1:242193529:1 REF",
    ">20 dna:chromosome chromosome:GRCh38:20:1:64444167:1 REF",
    ">21 dna:chromosome chromosome:GRCh38:21:1:46709983:1 REF",
    ">22 dna:chromosome chromosome:GRCh38:22:1:50818468:1 REF",
    ">3 dna:chromosome chromosome:GRCh38:3:1:198295559:1 REF",
    ">4 dna:chromosome chromosome:GRCh38:4:1:190214555:1 REF",
    ">5 dna:chromosome chromosome:GRCh38:5:1:181538259:1 REF",
    ">6 dna:chromosome chromosome:GRCh38:6:1:170805979:1 REF",
    ">7 dna:chromosome chromosome:GRCh38:7:1:159345973:1 REF",
    ">8 dna:chromosome chromosome:GRCh38:8:1:145138636:1 REF",
    ">9 dna:chromosome chromosome:GRCh38:9:1:138394717:1 REF",
    ">X dna:chromosome chromosome:GRCh38:X:1:156040895:1 REF",
    ">Y dna:chromosome chromosome:GRCh38:Y:2781480:56887902:1 REF"
]

if __name__ == '__main__':

    sites = 0
    line_end = ""

    with open('F:/Homo_sapiens.GRCh38.dna.primary_assembly.fa', 'r') as f:
        for line in f:
            if '>' in line:
                print("Number of sites: " + str(sites))
                print(line, end='')
            if '>' in line and not any(ident in line for ident in identifiers):
                print(line, end='')
                break
            elif '>' not in line:
                new_line = line_end + line
                sites += new_line.count('ATG')
                sites += new_line.count('CAT')

                if 'A\n' in line:
                    line_end = 'A'
                elif 'AT\n' in line:
                    line_end = 'AT'
                elif 'C\n' in line:
                    line_end = 'C'
                elif 'CA\n' in line:
                    line_end = 'CA'
                else:
                    line_end = ""
