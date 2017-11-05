###
### Testing only to retrieve patterns in nucleotides retrieved
### from the retrieve_seq.py module
###

import sys
import retrieve_seq  # module that is part of the alternative splice site project
import retrieve_pattern  # module that is part of the alternative splice site project

def find_pattern(arg_pattern, arg_seq, arg_print=''):
    rtn_pattern_list = []
    #  retrieve the full nucleotide sequence (the data to be searched) based on the accession#
    tmp_output_cumseq = retrieve_seq.get_seq(arg_seq, arg_print)
    # create the class object that contains the search pattern and data to be searched
    cls_pattern_list = retrieve_pattern.cls_sequence(arg_pattern, tmp_output_cumseq)
    rtn_pattern_list = cls_pattern_list.rtn_pattern_to_callingprogram(arg_print)
    if(arg_print == 'Y'):
        print("Result from calling program for ", arg_pattern)
    return rtn_pattern_list

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
    tmp_input_searchpattern = ''
    tmp_input_accession = ''
    tmp_input_print = ''

    if(len(sys.argv) == 1):
        raise ValueError('Search pattern is mandatory for the first argument for this program')
    else:
        tmp_input_searchpattern = str(sys.argv[1])

    if(len(sys.argv) == 2):
        raise ValueError('Accession number is mandatory for this program')
    else:
        tmp_input_accession = str(sys.argv[2])
    # if second (print/debug) argument exists, but is not 'Y', just default to blank/empty string
    if(len(sys.argv) == 4):
        if(sys.argv[3] != 'Y'):
            tmp_input_print = ''
        else:
            tmp_input_print = sys.argv[3]

    find_pattern(tmp_input_searchpattern, tmp_input_accession, tmp_input_print)
