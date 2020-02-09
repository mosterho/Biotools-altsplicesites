#Addition to Biotools Alternative Splice site project
##Intro
**Biotools** is an ongoing project at Ramapo College of NJ of the Bioinformatics program. It is headed-up by Dr. Bagga and Dr. Frees. The purpose of the project is to create a customized database of Chromosome sequences, mRNA, etc.

This folder contains additional self-assigned programs that I wrote to keep the skills I learned intact.

One self-assigned project was to find nucleotides in the SEQ collection in the "chrome" Mongo database that is part of the Biotools project. It can search for a nucleotide pattern using a REGEX pattern and return the from/to positions that were found.

##Details of the nucleotide search
The modules are:
1. *find_pattern.py* Validates input and calls the next two modules (in the following order)
2. *retrieve_seq.py* Retrieves the genome/nucleotides for a species and nucleotide accession number.
### Arguments are: Organism, Accession number, print (Y) (optional)
3. *retrieve_pattern* Determines the from/to positions in the retrieved sequence from *retrieve_seq.py*

retrieve_seq.py and retrieve_pattern.py can be called separately.

The call to the *find_pattern.py* accepts four arguments:
  1. Search pattern. This can accept the REGEX pattern to search for.
  2. Organism. This accepts the string version, not the taxon number (e.g., "Homo sapiens").
  3. Nucleotide accession number (optional): this can be "NC_000001", etc.
  4. Print Y/N (optional): this will print debugging information. In the python scripts in this folder, there are sections commented out. If uncommented, these lines will work, but will produce a lot of information.

##Examples
The following calls to the *find_pattern.py* python module seem to be successful:

###Looking for a transcription start codon (ATG=Methionine)
python3 find_pattern.py 'ATG' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  4038577
Result from calling program for  ATG

###Looking for individual stop codons...
python3 find_pattern.py 'TAA' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  4503830
Result from calling program for  TAA

python3 find_pattern.py 'TAG' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  2893538
Result from calling program for  TAG

python3 find_pattern.py 'TGA' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  4387595
Result from calling program for  TGA

###but then do the three totals above add up to the next one? ... (yes)
python3 find_pattern.py '(TAA|TAG|TGA)' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  11784963
Result from calling program for  (TAA|TAG|TGA)

### DOING THE FOLLOWING (remove the nucleotide accession#) 
### requires additional memory and large SWAP file (~40+Gb total physical and virtual)
python3 find_pattern.py '(TAA|TAG|TGA)' 'Homo sapiens' '' 'Y'

###Note the following when searching for a protein:
python3 find_pattern.py 'ATG+[ATCG]+(TAA|TAG|TGA)' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  38
Result from calling program for  ATG+[ATCG]+(TAA|TAG|TGA)

###but...:
python3 find_pattern.py 'ATG+(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  220797
Result from calling program for  ATG+(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)

###and...:
python3 find_pattern.py 'TATA+(?=[ATCG])+ATG(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  2475
Result from calling program for  TATA+(?=[ATCG])+ATG(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)


###Searching the entire human genome may take a few minutes...
python3 find_pattern.py 'ATG+(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' 'Homo sapiens' '' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:    is complete
Print number of match objects:  2953012
Result from calling program for  ATG+(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)

python3 find_pattern.py 'TATA+(?=[ATCG])+ATG(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' 'Homo sapiens' '' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:    is complete
Print number of match objects:  33515
Result from calling program for  TATA+(?=[ATCG])+ATG(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)

### this also worked using [ATCG]{3}...
python3 find_pattern.py 'TATA+(?=[ATCG])+ATG(?=[ATCG]{3})+(TAA|TAG|TGA)' 'Homo sapiens' '' 'Y'
retrieving data for pattern  TATA+(?=[ATCG])+ATG(?=[ATCG]{3})+(TAA|TAG|TGA)

Cumulative SEQ data values for: Homo sapiens accession:  is complete,  3095677412 nucleotides retrieved
Print number of match objects:  33515
Result from calling program for  TATA+(?=[ATCG])+ATG(?=[ATCG]{3})+(TAA|TAG|TGA)

