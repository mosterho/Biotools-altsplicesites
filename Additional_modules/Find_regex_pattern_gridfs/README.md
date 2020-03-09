#Addition to Biotools Alternative Splice site project
##Intro
**Biotools** is an ongoing project at Ramapo College of NJ of the Bioinformatics program. It is headed-up by Dr. Bagga and Dr. Frees. The purpose of the project is to create a customized database of Chromosome sequences, mRNA, etc.

This folder contains another project of additional self-assigned programs that I wrote to keep the skills I learned intact.

This self-assigned project is to find nucleotides via search string in the GridFS collection in a new "Chromosome" Mongo database. This database is not part of the original Biotools project. Data were initially loaded via mongofiles module that created a GridFS style database. 

The difference in calling the main program is that it uses the Python ArgParse method of working with parameters and arguments. This still searches for a nucleotide pattern using a REGEX pattern and returns the from/to positions that were found via iterable match objects.

##Details of the nucleotide search
The modules are:
1. *Main_program_regex_chromosome_find.py* Validates input and calls the following modules (in the following order)
2. *Build_chromosome_list.py* Creates a class that contains a list of chromosomes selected, calls "Chromosome_object" module to create individual class objects containing info on nucleotides, etc. Then calls "Find_regex" module to perform the search and create an iterable match object.
3. *chromosome_object.py* Retrieves the genome/nucleotides for a species and nucleotide accession number from the GridFS database. Creates a "chromosome" class containing the nucleotide sequence, etc. 
4. *Find_regex.py* Determines the from/to positions in the retrieved sequence from *Build_chromosome_list.py* and creates an iterable match object with SCAN positions.

All of the Python programs can be called separately with the appropriate parameters.

The call to the *main_program_regex_chromosome_find.py* accepts four parameters/arguments:
1. Taxon (integer): This is the numeric equivalent of species (e.g., 9606 is homo Sapiens).
2. Chromosome (string): This is a list of chromosomes entered as one or two characters prefaced with -c (e.g., -c 1 2 3 X Y)
3. SearchPattern (string): The regex search pattern to look for, enclosed in single quotes prefaced with -s (e.g., -s 'TATA+(TAA|TAG|TGA)'). 
4. Verbose (flag, optional): this will print debugging information. Values include omitting an entry or -v or -vv.
5. help (flag, optional): Taking advantage of ArgParse's abilities, help is displayed by adding -h at the end of the call

##Examples
The following calls to the *Main_program_regex_chromosome_find.py* python module:

###Looking for transcription start codon "ATG" in chromosomes 1 and 2, but adding -h flag for help
python3 Main_program_regex_chromosome_find.py 9606 -c 1  -s 'ATG' -v -h
usage: Search chromosome(s) in the GridFS system for a pattern. The arugments accepted include: a single taxon; multiple chromsome numbers (1 2 X Y); a search pattern; verbose output option

positional arguments:
  Taxon                 the taxon is the numeric ID of the species (e.g., 9606
                        is homo Sapiens)

optional arguments:
  -h, --help            show this help message and exit
  -c [CHROMOSOME [CHROMOSOME ...]], --chromosome [CHROMOSOME [CHROMOSOME ...]]
                        the chromosome number of the species. This will accept
                        multiple values (e.g., 1 2 4 X MT)
  -s SEARCHPATTERN, --SearchPattern SEARCHPATTERN
                        the regex search pattern to look for in the
                        chromosome(s)
  -v, --verbose         Specifiy the level of vebose output, valid values are
                        -v and -vv


###Looking for a transcription start codon (ATG=Methionine) with -v flag
python3 Main_program_regex_chromosome_find.py 9606 -c 1  -s 'ATG' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  ATG
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(803, 806), match='ATG'>, <_sre.SRE_Match object; span=(877, 880), match='ATG'>, <_sre.SRE_Match object; span=(953, 956), match='ATG'>, <_sre.SRE_Match object; span=(1487, 1490), match='ATG'>, <_sre.SRE_Match object; span=(1517, 1520), match='ATG'>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete


###Looking for the same transcription start codon "ATG", but with -vv flag
python3 Main_program_regex_chromosome_find.py 9606 -c 1  -s 'ATG' -vv
__main__   Main_program_regex_chromosome_find.py   Result of the parser is:  Namespace(SearchPattern='ATG', Taxon=9606, chromosome=['1'], verbose=2)
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  ATG
__main__  called from:  Main_program_regex_chromosome_find.py   Result of the creating container is:  <__main__.cls_overall_container object at 0x7f89166579b0>
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   ['chromosome1']
chromosome_object  called from:  Main_program_regex_chromosome_find.py   print ID/cursor object for grid.find({"filename":9606_chromosome1}): 
chromosome_object  called from:  Main_program_regex_chromosome_find.py   <gridfs.grid_file.GridOutCursor object at 0x7f891666f4a8>

use FOR loop to print the first 5 lines of the list
b'>gi|568815364|ref|NT_077402.3| Homo sapiens chromosome 1 genomic scaffold, GRCh38.p7 Primary Assembly HSCHR1_CTG1'
b'TAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAAC'
b'CCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCAACCCTAACCCTAACCCTAACCCTAACCCTAA'
b'CCCTAACCCCTAACCCTAACCCTAACCCTAACCCTAACCTAACCCTAACCCTAACCCTAACCCTAACCCT'
b'AACCCTAACCCTAACCCTAACCCCTAACCCTAACCCTAAACCCTAAACCCTAACCCTAACCCTAACCCTA'

print dataread_actual_firstline - should be first line of chromosome file
b'>gi|568815364|ref|NT_077402.3| Homo sapiens chromosome 1 genomic scaffold, GRCh38.p7 Primary Assembly HSCHR1_CTG1'
print dataread_actual_list after pop - should be only nucleotides
b'TAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAAC'
b'CCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCAACCCTAACCCTAACCCTAACCCTAACCCTAA'
b'CCCTAACCCCTAACCCTAACCCTAACCCTAACCCTAACCTAACCCTAACCCTAACCCTAACCCTAACCCT'
b'AACCCTAACCCTAACCCTAACCCCTAACCCTAACCCTAAACCCTAAACCCTAACCCTAACCCTAACCCTA'
b'ACCCTAACCCCAACCCCAACCCCAACCCCAACCCCAACCCCAACCCTAACCCCTAACCCTAACCCTAACC'
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Nucleotide string:  
 b'TAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAAC'
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Nucleotide string:  
 b'CCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCAACCCTAACCCTAACCCTAACCCTAACCCTAA'
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Nucleotide string:  
 b'CCCTAACCCCTAACCCTAACCCTAACCCTAACCCTAACCTAACCCTAACCCTAACCCTAACCCTAACCCT'
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Nucleotide string:  
 b'AACCCTAACCCTAACCCTAACCCCTAACCCTAACCCTAAACCCTAAACCCTAACCCTAACCCTAACCCTA'
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Nucleotide string:  
 b'ACCCTAACCCCAACCCCAACCCCAACCCCAACCCCAACCCCAACCCTAACCCCTAACCCTAACCCTAACC'
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Subset of the full Nucleotide string:  TAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCAACCCTAACCCT
Find_regex  called from:  Main_program_regex_chromosome_find.py   search pattern:  ATG
Find_regex  called from:  Main_program_regex_chromosome_find.py   Full match object reference:  <callable_iterator object at 0x7f8919dc8518>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(803, 806), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(877, 880), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(953, 956), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(1487, 1490), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(1517, 1520), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(1551, 1554), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(1609, 1612), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(1619, 1622), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(1718, 1721), match='ATG'>
Find_regex  called from:  Main_program_regex_chromosome_find.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(1744, 1747), match='ATG'>
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(803, 806), match='ATG'>, <_sre.SRE_Match object; span=(877, 880), match='ATG'>, <_sre.SRE_Match object; span=(953, 956), match='ATG'>, <_sre.SRE_Match object; span=(1487, 1490), match='ATG'>, <_sre.SRE_Match object; span=(1517, 1520), match='ATG'>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete


###Looking for individual stop codons...
python3 find_pattern.py 'TAA' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  4503830
Result from calling program for  TAA

#### but using new program
python3 Main_program_regex_chromosome_find.py 9606 -c 1 -s 'TAA' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  TAA
Find_regex  called from:  Main_program_regex_chromosome_find.py   total matches found:  4693288
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(0, 3), match='TAA'>, <_sre.SRE_Match object; span=(6, 9), match='TAA'>, <_sre.SRE_Match object; span=(12, 15), match='TAA'>, <_sre.SRE_Match object; span=(18, 21), match='TAA'>, <_sre.SRE_Match object; span=(24, 27), match='TAA'>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete


python3 find_pattern.py 'TAG' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  2893538
Result from calling program for  TAG

#### but using new program
python3 Main_program_regex_chromosome_find.py 9606 -c 1 -s 'TAG' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  TAG
Find_regex  called from:  Main_program_regex_chromosome_find.py   total matches found:  3039352
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(807, 810), match='TAG'>, <_sre.SRE_Match object; span=(957, 960), match='TAG'>, <_sre.SRE_Match object; span=(1132, 1135), match='TAG'>, <_sre.SRE_Match object; span=(1242, 1245), match='TAG'>, <_sre.SRE_Match object; span=(1268, 1271), match='TAG'>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete


python3 find_pattern.py 'TGA' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  4387595
Result from calling program for  TGA

### but using new program
python3 Main_program_regex_chromosome_find.py 9606 -c 1 -s 'TGA' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  TGA
Find_regex  called from:  Main_program_regex_chromosome_find.py   total matches found:  4619626
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(502, 505), match='TGA'>, <_sre.SRE_Match object; span=(507, 510), match='TGA'>, <_sre.SRE_Match object; span=(599, 602), match='TGA'>, <_sre.SRE_Match object; span=(1563, 1566), match='TGA'>, <_sre.SRE_Match object; span=(1568, 1571), match='TGA'>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete


###but then do the three totals above add up to the next one? ... (yes)
python3 find_pattern.py '(TAA|TAG|TGA)' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  11784963
Result from calling program for  (TAA|TAG|TGA)

### but using the new program, the totals add up, but not to the old program
python3 Main_program_regex_chromosome_find.py 9606 -c 1 -s '(TAA|TAG|TGA)' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  (TAA|TAG|TGA)
Find_regex  called from:  Main_program_regex_chromosome_find.py   total matches found:  12352266
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(0, 3), match='TAA'>, <_sre.SRE_Match object; span=(6, 9), match='TAA'>, <_sre.SRE_Match object; span=(12, 15), match='TAA'>, <_sre.SRE_Match object; span=(18, 21), match='TAA'>, <_sre.SRE_Match object; span=(24, 27), match='TAA'>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete


###Note the following when searching for a protein:
python3 find_pattern.py 'ATG+[ATCG]+(TAA|TAG|TGA)' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  38
Result from calling program for  ATG+[ATCG]+(TAA|TAG|TGA)

### but using the new program
python3 Main_program_regex_chromosome_find.py 9606 -c 1 -s 'ATG+[ATCG]+(TAA|TAG|TGA)' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  ATG+[ATCG]+(TAA|TAG|TGA)
Find_regex  called from:  Main_program_regex_chromosome_find.py   total matches found:  143
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(803, 197658), match='ATGCTAGCGCGTCGGGGTGGAGGCGTGGCGCAGGCGCAGAGAGGCGCGC>, <_sre.SRE_Match object; span=(197786, 238051), match='ATGGCTGAAATCGTGTTTGACCAGCTATGTGTGTCTCTCAATCCGATCA>, <_sre.SRE_Match object; span=(238253, 426213), match='ATGCCTTGTTCTCTTTATCAGGACAAATCAGGGTGGTGACCTTGGCCAC>, <_sre.SRE_Match object; span=(426372, 2543099), match='ATGTGTGCATTTTCCTGAGAGGAAAGCTTTCCCACATTATTCAGCTTCT>, <_sre.SRE_Match object; span=(2586751, 12794718), match='ATGGTCTGGAGCAGCACCCACAACCACAGGTGAGCCTCTGACAGCCTGG>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete


###but...:
python3 find_pattern.py 'ATG+(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' 'Homo sapiens' 'NC_000001' 'Y'
Cumulative SEQ data values for  Homo sapiens accession:  NC_000001  is complete
Print number of match objects:  220797
Result from calling program for  ATG+(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)

### with the new program
python3 Main_program_regex_chromosome_find.py 9606 -c 1 -s 'ATG+(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  ATG+(?=[ATCG][ATCG][ATCG])+(TAA|TAG|TGA)
Find_regex  called from:  Main_program_regex_chromosome_find.py   total matches found:  314962
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(1814, 1820), match='ATGTAG'>, <_sre.SRE_Match object; span=(2141, 2147), match='ATGTAA'>, <_sre.SRE_Match object; span=(2548, 2555), match='ATGGTAG'>, <_sre.SRE_Match object; span=(7075, 7081), match='ATGTGA'>, <_sre.SRE_Match object; span=(7767, 7774), match='ATGGTGA'>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete

### with the new program, remove the '?=' and first '+'
python3 Main_program_regex_chromosome_find.py 9606 -c 1 -s 'ATG([ATCG][ATCG][ATCG])+(TAA|TAG|TGA)' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  ATG([ATCG][ATCG][ATCG])+(TAA|TAG|TGA)
Find_regex  called from:  Main_program_regex_chromosome_find.py   total matches found:  169
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(803, 197651), match='ATGCTAGCGCGTCGGGGTGGAGGCGTGGCGCAGGCGCAGAGAGGCGCGC>, <_sre.SRE_Match object; span=(197786, 237851), match='ATGGCTGAAATCGTGTTTGACCAGCTATGTGTGTCTCTCAATCCGATCA>, <_sre.SRE_Match object; span=(237861, 238047), match='ATGACCATTTGGCCAGAATTTATGAACTCTACATGTCGCTTGATGTGTG>, <_sre.SRE_Match object; span=(238253, 426206), match='ATGCCTTGTTCTCTTTATCAGGACAAATCAGGGTGGTGACCTTGGCCAC>, <_sre.SRE_Match object; span=(426372, 2543067), match='ATGTGTGCATTTTCCTGAGAGGAAAGCTTTCCCACATTATTCAGCTTCT>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete

### but to get really fancy, use '?=' for the stop codon... but notice the difference in total matches!
python3 Main_program_regex_chromosome_find.py 9606 -c 1 -s 'ATG([ATCG][ATCG][ATCG])+(?=TAA|TAG|TGA)' -v
__main__  called from:  Main_program_regex_chromosome_find.py 
Taxon is:  9606 
chromosome(s):  ['chromosome1'] 
Search Pattern:  ATG([ATCG][ATCG][ATCG])+(?=TAA|TAG|TGA)
Find_regex  called from:  Main_program_regex_chromosome_find.py   total matches found:  172
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   a subset of the returned match object is:  [<_sre.SRE_Match object; span=(803, 197648), match='ATGCTAGCGCGTCGGGGTGGAGGCGTGGCGCAGGCGCAGAGAGGCGCGC>, <_sre.SRE_Match object; span=(197786, 237848), match='ATGGCTGAAATCGTGTTTGACCAGCTATGTGTGTCTCTCAATCCGATCA>, <_sre.SRE_Match object; span=(237861, 238044), match='ATGACCATTTGGCCAGAATTTATGAACTCTACATGTCGCTTGATGTGTG>, <_sre.SRE_Match object; span=(238253, 426203), match='ATGCCTTGTTCTCTTTATCAGGACAAATCAGGGTGGTGACCTTGGCCAC>, <_sre.SRE_Match object; span=(426372, 2543064), match='ATGTGTGCATTTTCCTGAGAGGAAAGCTTTCCCACATTATTCAGCTTCT>]
Build_chromosome_list  called from:  Main_program_regex_chromosome_find.py   Class object for  chromosome1  complete


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



##THIS WORKS, the previous ones from my school project may have never worked, esp. when using '?=' ('+' should work as well as '*') (2 Mar 2020)
python3 Main_program_regex_chromosome_find.py 9606 -c  X Y -s 'TATA([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)' -vv


##THIS WORKS, testing the Find_regex.py module, including an extra 'A' after 'TATA'
First example tests for the extra 'A', but is not in the data
The second example contains the extra 'A' in the data.
Note the difference in the lengths returned (span=).
NOTE: the 'A?' is not necessary, since '([ATCG])' should account for the extra 'A' for the TATA box.

### without 'A?' does not include extra 'A' in data
python3 Find_regex.py 'TATA([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)'  'CGTGCTGTTATACGTCGTCGTCGTCGTGCTGCTATGCGTCGTCGTCGTCGTCGTCGTCGTCGTCCGTCGTCGCTTTGGGCCCGGGTTTCCCGTTTCCCGGGTTTGGGTTTGGGCCCGGGTTTGGGTTTCCCTGCGCTTTTTTTTTTTTCCCCCCCCCGGGGGGTTTGGGCCCGTGCGTCGTGTCGTCGTCGTCGTCGTTGCTGCTGCGGTCCGTAGATG' 2
__main__  called from:  Find_regex.py   search pattern:  TATA([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)
__main__  called from:  Find_regex.py   Full match object reference:  <callable_iterator object at 0x7f32e5ca2ba8>
__main__  called from:  Find_regex.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(8, 216), match='TATACGTCGTCGTCGTCGTGCTGCTATGCGTCGTCGTCGTCGTCGTCGT>
__main__  called from:  Find_regex.py   total matches found:  1

### with 'A?' does not include extra 'A' in data
python3 Find_regex.py 'TATAA?([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)'  'CGTGCTGTTATACGTCGTCGTCGTCGTGCTGCTATGCGTCGTCGTCGTCGTCGTCGTCGTCGTCCGTCGTCGCTTTGGGCCCGGGTTTCCCGTTTCCCGGGTTTGGGTTTGGGCCCGGGTTTGGGTTTCCCTGCGCTTTTTTTTTTTTCCCCCCCCCGGGGGGTTTGGGCCCGTGCGTCGTGTCGTCGTCGTCGTCGTTGCTGCTGCGGTCCGTAGATG' 2
__main__  called from:  Find_regex.py   search pattern:  TATAA?([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)
__main__  called from:  Find_regex.py   Full match object reference:  <callable_iterator object at 0x7f2b5fd3dba8>
__main__  called from:  Find_regex.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(8, 216), match='TATACGTCGTCGTCGTCGTGCTGCTATGCGTCGTCGTCGTCGTCGTCGT>

### without 'A?' does include extra 'A' in data
python3 Find_regex.py 'TATA([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)'  'CGTGCTGTTATAACGTCGTCGTCGTCGTGCTGCTATGCGTCGTCGTCGTCGTCGTCGTCGTCGTCCGTCGTCGCTTTGGGCCCGGGTTTCCCGTTTCCCGGGTTTGGGTTTGGGCCCGGGTTTGGGTTTCCCTGCGCTTTTTTTTTTTTCCCCCCCCCGGGGGGTTTGGGCCCGTGCGTCGTGTCGTCGTCGTCGTCGTTGCTGCTGCGGTCCGTAGATG' 2
__main__  called from:  Find_regex.py   search pattern:  TATA([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)
__main__  called from:  Find_regex.py   Full match object reference:  <callable_iterator object at 0x7f913026aba8>
__main__  called from:  Find_regex.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(8, 217), match='TATAACGTCGTCGTCGTCGTGCTGCTATGCGTCGTCGTCGTCGTCGTCG>
__main__  called from:  Find_regex.py   total matches found:  1

### with 'A?' does include extra 'A' in data
python3 Find_regex.py 'TATAA?([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)'  'CGTGCTGTTATAACGTCGTCGTCGTCGTGCTGCTATGCGTCGTCGTCGTCGTCGTCGTCGTCGTCCGTCGTCGCTTTGGGCCCGGGTTTCCCGTTTCCCGGGTTTGGGTTTGGGCCCGGGTTTGGGTTTCCCTGCGCTTTTTTTTTTTTCCCCCCCCCGGGGGGTTTGGGCCCGTGCGTCGTGTCGTCGTCGTCGTCGTTGCTGCTGCGGTCCGTAGATG' 2
__main__  called from:  Find_regex.py   search pattern:  TATAA?([ATCG])*ATG([ATCG]{3})*(TAA|TAG|TGA)
__main__  called from:  Find_regex.py   Full match object reference:  <callable_iterator object at 0x7fcd59b35ba8>
__main__  called from:  Find_regex.py   print only 1st 10 matches:  <_sre.SRE_Match object; span=(8, 217), match='TATAACGTCGTCGTCGTCGTGCTGCTATGCGTCGTCGTCGTCGTCGTCG>


