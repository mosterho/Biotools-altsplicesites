###
### Testing only to retrieve and decompress the nucleotides in the seq collection
###

import sys
import zlib
import binascii
import pymongo

def get_seq(arg_accession, arg_print=''):

    # create objects required to access MongoDB
    from pymongo import MongoClient
    client = MongoClient('10.20.20.5', 27017)
    db = client.chrome
    collection_seq = db.seq

    # define work fields for this def
    wrk_cumulativeseqs = ''
    cursor = collection_seq.find({"accession":arg_accession})
    for rowdata in cursor:
        ### all of the following is just to show progression of reversing the binary data conversion and
        ### and decompression of the "SEQ" attribute of SEQ collection
        #print("Raw row info: ",(rowdata))
        #print("\nseq data only compressed but binary: ", rowdata['seq'])
        #print("\nseq data only decompressed, still binary: ", zlib.decompress(rowdata['seq']))
        #print("\nseq data only decompressed, STR(): ", str(zlib.decompress(rowdata['seq'])))
        #print("\nseq data only decompressed, STR() and decode: ", str(zlib.decompress(rowdata['seq']).decode('ascii')))
        wrk_cumulativeseqs += str(zlib.decompress(rowdata['seq']).decode('ascii'))

    if(arg_print == 'Y'):
        print("\nCumulative SEQ data values for ", arg_accession," is: ", wrk_cumulativeseqs)
    return wrk_cumulativeseqs


#-------------------------------------------------------------------------------
#### begin mainline
## first argument is gene accession number
## second argument is optional, if "Y" print debugging info

### for coding, consider adding the following for debugging:
### if 0, do not print any info
### if 1, print detailed info in functions
### if 2, similiar to option 1, but to log file only (not to screen)

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):
    tmp_input_accession = ''
    tmp_input_print = ''
    tmp_output_cumseq = ''

    if(len(sys.argv) == 1):
        raise ValueError('Accession number is mandatory for the first argument for this program')
    else:
        tmp_input_accession = str(sys.argv[1])

    # if second (print/debug) argument exists, but is not 'Y', just default to blank/empty string
    if(len(sys.argv) == 3):
        if(sys.argv[2] != 'Y'):
            tmp_input_print = ''
        else:
            tmp_input_print = sys.argv[2]

    tmp_output_cumseq = get_seq(tmp_input_accession, tmp_input_print)
    #return tmp_output_cumseq
