'''
    Find search patterns of nucleotides from the SEQ collection of the MongoDB "chrome" database.
    First retrieve the full sequence of nucleotides from the SEQ collection
    Create a class object that contains the search sequence and the data to be searched
    Return a list of tuples containing the from/to positions of the search pattern found.
    The search pattern works as a regex using "finditer"
'''

import sys
import retrieve_seq  # module that is part of the alternative splice site project
import retrieve_pattern  # module that is part of the alternative splice site project
import pymongo

def get_pattern(arg_pattern, arg_organism, arg_accessionnbr='', arg_print=''):
    ## this validates the entries passed to this program/module.
    ## if the combination of organism/chromosome accession number are invalid,
    ## return "false" to the calling program, otherwise continue
    wrk_return = validate_arguments(arg_pattern, arg_organism, arg_accessionnbr, arg_print)
    if(wrk_return == 0):
        return
    if(arg_print == 'Y'):
        print("retrieving data for pattern ", arg_pattern)
    rtn_pattern_list = []  # returns a list of tuples containing from/to positions
    #  retrieve the full nucleotide sequence (the data to be searched)
    tmp_output_cumseq = retrieve_seq.get_seq(arg_organism, arg_accessionnbr, arg_print)
    # create the class object that contains the search pattern and data to be searched
    cls_pattern_list = retrieve_pattern.cls_sequence(arg_pattern, tmp_output_cumseq)
    # return a list of tuples containing the from/to positions of the found data
    rtn_pattern_list = cls_pattern_list.rtn_pattern_to_callingprogram(arg_print)
    if(arg_print == 'Y'):
        print("Result from calling program for ", arg_pattern)
    return rtn_pattern_list

def validate_arguments(arg_pattern, arg_organism, arg_accessionnbr, arg_print=''):
    # create objects required to access MongoDB
    from pymongo import MongoClient
    #client = MongoClient('10.20.20.5', 27017)
    client = MongoClient('Ubuntu18Server01')
    db = client.chrome
    collection_seq = db.seq

    if(arg_accessionnbr == ''):
        cursor = collection_seq.find({"organism":arg_organism}).limit(1)
    else:
        cursor = collection_seq.find({"organism":arg_organism, "accession":arg_accessionnbr}).limit(1)

    # if at least one entry is found, return "true"
    for wrk_row in cursor:
        return(1)
    print('No entries found for ', arg_organism, ' and accession: ', arg_accessionnbr)
    return(0)

#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):
    tmp_input_searchpattern = ''
    tmp_input_organism = ''
    tmp_input_accessionnbr = ''
    tmp_input_print = ''

    if(len(sys.argv) == 1):
        raise ValueError('Search pattern is mandatory for the first argument for this program')
    else:
        tmp_input_searchpattern = str(sys.argv[1])

    if(len(sys.argv) == 2):
        raise ValueError('Organism is mandatory for this program')
    else:
        tmp_input_organism = str(sys.argv[2])

    # accession number can be any value, watch positions for next argument though...
    if(len(sys.argv) >= 4):
        tmp_input_accessionnbr = str(sys.argv[3])

    # if second (print/debug) argument exists, but is not 'Y', just default to blank/empty string
    if(len(sys.argv) == 5):
        if(sys.argv[4] != 'Y'):
            tmp_input_print = ''
        else:
            tmp_input_print = sys.argv[4]

    rtn_pattern_list = get_pattern(tmp_input_searchpattern, tmp_input_organism, tmp_input_accessionnbr, tmp_input_print)
