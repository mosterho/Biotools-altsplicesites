###
### Testing only to retrieve patterns in nucleotides retrieved
### from the retrieve_seq.py module
###

import sys
import re #regex searches

class cls_sequence:

    def __init__(self, arg_pattern, arg_seq):
        ### arg_pattern contains the search pattern
        ### arg_seq contains the data to search
        self.cls_pattern = arg_pattern
        self.cls_seq = arg_seq

    def get_pattern(self, arg_print='N'):
        ### use regex (finditer) to find the pattern,
        ### build a list of arg_seq "regex match" objects
        wrk_result = []

        ### re.finditer is the important piece of this module.
        ### this is used to search Regex patterns
        ### returns a regex match object, add to wrk_result
        for wrk_found in re.finditer(self.cls_pattern, self.cls_seq):
            wrk_result.append(wrk_found)
            #if(arg_print == 'Y'):
                #print("wrk_found: " + str(wrk_found))
        #if(arg_print == 'Y'):
            #print("Final list of regex match objects: ", wrk_result)
        return wrk_result

    def rtn_pattern_list(self, arg_matchobject, arg_print=''):
        # use this routine to accept the regex match object and break it down
        # to a list of tuples (from/to positions) to be sent back to the calling program
        rtn_list = []
        rtn_count = 0
        if (arg_matchobject):
            for wrk_result in arg_matchobject:
                ### span() contains the from/to positions of the match object for the string.
                rtn_list.append(wrk_result.span())
                rtn_count += 1
                #if(arg_print == 'Y'):
                    #print("within rtn_pattern_list: ", wrk_result)
                    #print("printing group: ", wrk_result.group())  # responds with seatch pattern
                    #print("printing span: ", wrk_result.span())  # contains the from/to positions
                    #print("printing groups: ", wrk_result.groups())  # nothing
        if(arg_print == 'Y'):
            #print("print pattern of list of tuples: ", rtn_list)
            print("Print number of match objects: ",rtn_count)
        return rtn_list

    def rtn_pattern_to_callingprogram(self, arg_print=''):
        # this routine combines both defined above.
        # retrieve a regex match object, then break down to a list of tuples
        # of from/to positions of the matched pattern
        rtn_list = []
        wrk_result = self.get_pattern(arg_print)
        rtn_list = self.rtn_pattern_list(wrk_result, arg_print)

        return rtn_list

#-------------------------------------------------------------------------------
#### begin mainline
#-------------------------------------------------------------------------------

if (__name__ == "__main__"):
    tmp_input_pattern = ''
    tmp_input_seq = ''
    tmp_input_print = ''
    tmp_return_matchobject_list = []

    if(len(sys.argv) == 1):
        raise ValueError('search pattern is mandatory for the first argument for this program')
    else:
        tmp_input_pattern = str(sys.argv[1])

    if(len(sys.argv) == 2):
        raise ValueError('Search content/data is mandatory for the second argument for this program')
    else:
        tmp_input_seq = str(sys.argv[2])

    # if print/debug argument exists, but is not 'Y', just default to blank/empty string
    if(len(sys.argv) == 4):
        if(sys.argv[3] != 'Y'):
            tmp_input_print = ''
        else:
            tmp_input_print = str(sys.argv[3])

    '''
    After initializing the arguments passed in to this program,
    create class object "tmp_seq_obj" that holds the search pattern
    and the data to be searched.
    the "tmp_return_matchobject_list" returned from the "rtn_pattern_to_callingprogram" module
    will return a list of tuples containing the from/to positions of the matches as:
    [(from position, to position), (from position, to position), ...]
    Note: the "from position" is similar to index positions, i.e. starts at 0
          and the "to" position is actually the start position of the next string position
          and has nothing to do with the length of the pattern that was found,
          but can be used to determine the length of the found string (end pos - start pos)
    '''
    tmp_seq_obj = cls_sequence(tmp_input_pattern, tmp_input_seq)
    tmp_return_matchobject_list = tmp_seq_obj.rtn_pattern_to_callingprogram(tmp_input_print)
