'''
    Retrieve and decompress the nucleotides in the seq collection
    from the mongodb database
    Argument is organism (e.g., Homo sapiens), accession#, print
'''

import sys
import zlib
#import binascii
import pymongo

def get_seq(arg_organism, arg_accessionnbr, arg_print=''):

    # create objects required to access MongoDB
    from pymongo import MongoClient
    client = MongoClient('Ubuntu18Server01')
    db = client.chrome
    collection_seq = db.seq

    # define work fields for this def
    wrk_cumulativeseqs = ''

    if(arg_accessionnbr == ''):
        cursor = collection_seq.find({"organism":arg_organism}).sort([("accession", pymongo.ASCENDING),("start", pymongo.ASCENDING)])
    else:
        cursor = collection_seq.find({"organism":arg_organism, "accession":arg_accessionnbr}).sort([("accession", pymongo.ASCENDING),("start", pymongo.ASCENDING)])
    for rowdata in cursor:
        wrk_cumulativeseqs += str(zlib.decompress(rowdata['seq']).decode('ascii'))

    if(arg_print == 'Y'):
        #print(wrk_cumulativeseqs)
        print("\nCumulative SEQ data values for:", arg_organism, "accession:", arg_accessionnbr, "is complete, ", len(wrk_cumulativeseqs), "nucleotides retrieved")
    return wrk_cumulativeseqs


#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):
    tmp_input_organism = ''
    tmp_input_accessionnbr = ''
    tmp_input_print = ''
    tmp_output_cumseq = ''

    if(len(sys.argv) == 1):
        raise ValueError('Organism is mandatory for this program')
    else:
        tmp_input_organism = str(sys.argv[1])

    # accession number can be any value, watch positions for next argument though...
    if(len(sys.argv) >= 3):
        tmp_input_accessionnbr = str(sys.argv[2])

    # if second (print/debug) argument exists, but is not 'Y', just default to blank/empty string
    if(len(sys.argv) == 4):
        if(sys.argv[3] != 'Y'):
            tmp_input_print = ''
        else:
            tmp_input_print = sys.argv[3]

    tmp_output_cumseq = get_seq(tmp_input_organism, tmp_input_accessionnbr, tmp_input_print)
