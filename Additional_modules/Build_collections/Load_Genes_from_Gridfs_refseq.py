
## Build a single gene collection
## from the refseq NCBI files

import sys
from pymongo import MongoClient
import gridfs, re

client = MongoClient('mongodb')
db = client.refseqgene
fs_forwrite = db.refseqgene_file  # for writing to a new file
fs_forread  = gridfs.GridFSBucket(db)

## delete any entries in refseqgene_file before starting
print('perform "delete_many" on existing refseqgene collection')
fs_forwrite.delete_many({})

wrk_accession_break = ''
first_read = False

for fs_find in fs_forread.find({}):
    fs_read = fs_find.read()
    print('fs_read: ', fs_read[:100])
    #
    fs_read_decode = fs_read.decode()
    fs_read_decode_splits = fs_read_decode.split("\n")
    for x_read in fs_read_decode_splits:
        if(x_read[:1] == ">"):
            if(first_read is True):
                Nucleotide_encoded = write_data.encode()
                fs_forwrite.insert_one({"accession_nbr":accession_nbr, "gene": gene_abbrev, "Description":description, "Nucleotides":Nucleotide_encoded})
                print('accession: ', accession_nbr, 'gene abbrev: ', gene_abbrev, 'description: ', description)
            else:
                first_read = True
            accession_nbr = x_read[1:10]
            gene_abbrev_list = re.findall('(?<=[(]).+?(?=[)])', x_read)
            for x in gene_abbrev_list:
                gene_abbrev = x
            description = x_read[13:]
            write_data = x_read
        else:
            write_data += x_read
    Nucleotide_encoded = write_data.encode()
    fs_forwrite.insert_one({"accession_nbr":accession_nbr, "gene": gene_abbrev, "Description":description, "Nucleotides":Nucleotide_encoded})
    print('accession: ', accession_nbr, 'gene abbrev: ', gene_abbrev, 'description: ', description)
