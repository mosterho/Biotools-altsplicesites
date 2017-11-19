##Addition to Biotools Alternative Splice site project

**Biotools** is an ongoing project at Ramapo College of NJ Bioinformatics program. It is headed-up by Dr. Bagga and Dr. Frees. The purpose of the project is to create a customized database of Chromosome sequences, mRNA, etc.

This folder contains additional self-assigned programs that I wrote to keep the skills I learned intact.

One project was to write the PERL programming "translate reading frame" assignment to read any FASTA file passed into it.

Another project was to write modules that would unzip the SEQ collection in the "chrome" Mongo database that is part of the Biotools project. It can also search for a nucleotide pattern against the SEQ collection and return the from/to positions that were found. The search pattern can be a REGEX pattern. The following calls to the *find_pattern.py* python module seem to be successful:


python3 find_pattern.py 'ATG(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' 'Homo sapiens' '' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:    is complete
Print number of match objects:  2953012
Result from calling program for  ATG(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)


python3 find_pattern.py 'TATA+(?=[ATCG])+ATG(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' 'Homo sapiens' '' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:    is complete
Print number of match objects:  33515
Result from calling program for  TATA+(?=[ATCG])+ATG(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)
