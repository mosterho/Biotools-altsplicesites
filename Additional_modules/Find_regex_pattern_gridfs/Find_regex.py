
#
##  This program will find a regex pattern in a string of data
##  Accept two arguments: the regex pattern and a list to be searched
##  returns a list of match ITERATOR objects from FINDITER()

## see "retrieve_pattern" in Biotools folder for example code

import sys, re

def fnc_search(arg_searchpattern, arg_data, arg_verbose):

    parm_dataread = []  # return a list of iterator objects from FINDITER()

    if(arg_verbose >= 2):
        print(__name__, ' called from: ', sys.argv[0], ' ', 'search pattern: ', arg_searchpattern)
        #print('input data: ', arg_data)

    ## use finditer to create an "iterator" object to loop through
    ## note: finditer requires strings to search, not lists
    tmp_search = re.compile(arg_searchpattern)
    wrk_founddata = re.finditer(tmp_search, arg_data)
    if(arg_verbose >= 2):
        print(__name__, ' called from: ', sys.argv[0], ' ', 'Full match object reference: ', wrk_founddata)
    tmp_counter = 0
    for dataread in wrk_founddata:
        parm_dataread.append(dataread)
        tmp_counter += 1
        if(arg_verbose >= 2 and tmp_counter <= 10):
            print(__name__, ' called from: ', sys.argv[0], ' ', 'print 1st 10 matches: ',  dataread)
    if(dataread and arg_verbose >= 1):
        print(__name__, ' called from: ', sys.argv[0], ' ', 'total matches found: ', tmp_counter)
        print(__name__, ' called from: ', sys.argv[0], ' ', 'Number of nucleotides: ', '{:,}'.format(len(arg_data)))

    return parm_dataread

#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):

    if(len(sys.argv) == 1):
        raise ValueError('Search pattern is mandatory for the first argument for this program')
    else:
        tmp_input_searchpattern = sys.argv[1]

    if(len(sys.argv) == 2):
        raise ValueError('Data to be searched is mandatory for this program')
    else:
        tmp_input_data = sys.argv[2]

    # evaluate print/debug argument
    if(len(sys.argv) == 3):
        raise ValueError('Verbose flags are mandatory for this program')
    else:
        tmp_input_verbose = int(sys.argv[3])

    rtn_value = fnc_search(tmp_input_searchpattern, tmp_input_data, tmp_input_verbose)
