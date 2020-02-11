
##
## Main calling program to find a regex pattern in
## the NBCI MongoDB GridFS system.
##
## This behaves in a similar manner to the previous project,
## except that the modules work with the GridFS system.

import sys, Load_from_Gridfs_buckets

class cls_object:
    def __init__(self, arg_pattern, arg_seq):
        ### arg_pattern contains the search pattern
        ### arg_seq contains the data to search (assuming a byte string)
        self.cls_pattern = arg_pattern
        self.cls_seq = arg_seq

    def build_chromosome(self, arg_list, arg_debug):
        ### arg_list contains the bytelist of a chromsome, SPLIT off newline characters
        ### and return a byte "list"
        self.wrk_list = str(arg_list).split(b'\n')
        return self.wrk_list

    def 
