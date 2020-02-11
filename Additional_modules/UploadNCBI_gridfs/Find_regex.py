
#
##  This program will find a regex pattern in a string
##  Accept two arguments: the regex pattern and a list to be searched

## see "retrieve_pattern" in Biotools folder for example code

import re





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
        raise ValueError('Data to search is mandatory for this program')
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

    #get_pattern(tmp_input_searchpattern, tmp_input_organism, tmp_input_accessionnbr, tmp_input_print)
