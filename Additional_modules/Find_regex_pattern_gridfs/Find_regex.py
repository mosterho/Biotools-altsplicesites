
#
##  This program will find a regex pattern in a string of data
##  Accept two arguments: the regex pattern and a list to be searched
##  returns a list of match ITERATOR objects from FINDITER()

## see "retrieve_pattern" in Biotools folder for example code

import sys, re

def fnc_search(arg_searchpattern, arg_data, arg_debug=''):

    parm_dataread = []  # return a list of iterator objects from FINDITER()

    if(arg_debug == '-v' or arg_debug == '-vv'):
        print('search pattern: ', arg_searchpattern)
        print('input data: ', arg_data)

    ## use finditer to create an "iterator" object to loop through
    ## note: finditer requires strings to search, not lists
    wrk_founddata = re.finditer(arg_searchpattern, arg_data)
    for dataread in wrk_founddata:
        parm_dataread.append(dataread)
        if(arg_debug == '-vv'):
            print('found: ',  dataread)

    return parm_dataread

#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):
    #tmp_input_searchpattern = ''
    #tmp_input_data = []   # let the argument determine the data type, probably list of bytedata
    #tmp_input_print = ''

    if(len(sys.argv) == 1):
        raise ValueError('Search pattern is mandatory for the first argument for this program')
    else:
        tmp_input_searchpattern = sys.argv[1]

    if(len(sys.argv) == 2):
        raise ValueError('Data to be searched is mandatory for this program')
    else:
        tmp_input_data = sys.argv[2]

    # if print/debug argument exists, but is not valid, just default to blank/empty string
    if(len(sys.argv) == 4):
        if(sys.argv[3] != '-v' and sys.argv[3] != '-vv'):
            tmp_input_debug = ''
        else:
            tmp_input_debug = sys.argv[3]

    rtn_value = fnc_search(tmp_input_searchpattern, tmp_input_data, tmp_input_debug)
