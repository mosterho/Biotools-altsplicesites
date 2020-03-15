
## Build a single gene collection
## from the refseq NCBI files

import sys
from pymongo import MongoClient
import gridfs, re

client = MongoClient('mongodb')
db = client.protein
fs_forwrite = db.protein_file  # for writing to a new file
fs_forread  = gridfs.GridFSBucket(db)

## delete any entries in refseqgene_file before starting
print('perform "delete_many" on existing protein collection')
fs_forwrite.delete_many({})

#wrk_accession_break = ''
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
                AA_encoded = write_data.encode()
                #fs_forwrite.insert_one({"GI":gi_nbr, "ref": ref_abbrev, "Description":description, "Amino_acids":AA_encoded})
                print("GI ", gi_nbr, "ref ", ref_abbrev, "Description ", description)
            else:
                first_read = True
            #wrk_fieldbreak = re.findall('(?<=[|]).*?(?=[|])', x_read)
            wrk_fieldbreak  = re.findall('(?<=[|]).*?(?=[|])', x_read, re.DOTALL)
            wrk_description = re.findall('(((?<=[|]).*?){3}).*', x_read, re.DOTALL)
            print('fieldbreak: ', wrk_fieldbreak, ' ', wrk_description)
            gi_nbr = x_read[4:13]
            ref_abbrev = x_read[17:32]
            description = x_read[33:]
            write_data = x_read
        else:
            write_data += x_read
    AA_encoded = write_data.encode()
    #fs_forwrite.insert_one({"GI":gi_nbr, "ref": ref_abbrev, "Description":description, "Amino_acids":AA_encoded})
    print("GI ", gi_nbr, "ref ", ref_abbrev, "Description ", description)
