#!/usr/bin/python3
import os
import sys
import numpy

curr_path = os.path.realpath(__file__)
CHE550_path = curr_path[: curr_path.find('\\', curr_path.find("CHE550"))]
sys.path.append(CHE550_path)

import CHE550_tools

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

    chromosomes = dict()

    with open('F:/Homo_sapiens.GRCh38.dna.primary_assembly.fa', 'r') as f:

        chrom_id = str()
        end_t = False  # used incase the line ends with a T and the next line starts with T

        for line in f:
            # found header for chromosome
            if any(ident in line for ident in identifiers):
                if chrom_id:
                    print(chromosomes[chrom_id])
                print(line, end='')
                chrom_id = line  # set sentinel value
                chromosomes[chrom_id] = int()
                end_t = False
            # found a header other than chromosome
            elif '>' in line:
                if chrom_id:
                    print(chromosomes[chrom_id])
                chrom_id = str()
                end_t = False
            # sequence
            elif chrom_id:
                chromosomes[chrom_id] += len(CHE550_tools.DNA.find_dimer_sites(line))
                if line[0] == "T":
                    chromosomes[chrom_id] += 1
                if "T\n" in line:
                    end_t = True
                else:
                    end_t = False

    data = [chromosomes[chrom_id] for chrom_id in chromosomes]
    print("# dimer sites: " + str(numpy.sum(data)))
    print("AVG: " + str(numpy.mean(data)))
    print("STD: " + str(numpy.std(data)))
    print("Median: " + str(numpy.median(data)))
