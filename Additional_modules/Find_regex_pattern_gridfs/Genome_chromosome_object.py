
##
## This module will create a single chromosome object
## it will include the resulting nucleotides, but
## without the search pattern.
##
##  arguments:
##    arg_taxon = numeric value for species
##    arg_chromosome = string full name of a single chromosome such as 'chromosomeX'
##    arg_verbose = numeric equivalent from argparser (-vv = 2)

from pymongo import MongoClient
import sys, gridfs

class cls_chromosome_object:
    def __init__(self, arg_taxon, arg_chromosome, arg_verbose):

        self.cls_taxon = arg_taxon
        self.cls_chromosome = arg_chromosome
        self.cls_verbose = arg_verbose
        # self.nucleotides is created in the "build_chromosome" function below
        # self.chromosome_title is also created in the "build_chromosome" function
        self.cls_filename = str(self.cls_taxon) + '_' + self.cls_chromosome

    def build_chromosome(self):
        ### Use the class cls_seq to create the bytelist of a chromsome, SPLIT off newline characters
        ### and return a bytelist of nucleotides
        client = MongoClient('Ubuntu18Server01')
        db = client.Chromosome
        #fsfiles = db.fs.files
        grid  = gridfs.GridFSBucket(db)

        ##
        if(self.cls_verbose == 2):
            print(__name__, ' called from: ', sys.argv[0], ' ', 'print ID/cursor object for grid.find({"filename":' + self.cls_filename + '}): ')
            print(__name__, ' called from: ', sys.argv[0], ' ', grid.find({"filename":self.cls_filename}))
        ## Retrieve the data from GridFS basedon taxon_chromosome#
        for dataread in grid.find({"filename":self.cls_filename}):
            dataread_actual = dataread.read()
            # Create a list of byte data from the file/bucket, SPLIT off newline character
            # but keep the lines separate
            dataread_actual_bytelist = dataread_actual.split(b'\n')
            if(self.cls_verbose == 2):
                print('\nuse FOR loop to print the first 5 lines of the list')
                for i in range(5):
                    print(dataread_actual_bytelist[i])
            # Use POP to remove the first line (this contains the >gi|, description, etc.)
            # and keep the nucleotide data
            self.chromosome_title = dataread_actual_bytelist.pop(0)
            if(self.cls_verbose == 2):
                print('\nprint dataread_actual_firstline - should be first line of chromosome file')
                print(self.chromosome_title)
                print('print dataread_actual_list after pop - should be only nucleotides')
                for i in range(5):
                    print(dataread_actual_bytelist[i])
            # After using POP, this should contain only nucleotide data
            self.cls_nucleotides = dataread_actual_bytelist
        ## if dataread_actual contains data, OK, otherwise raise exception error
        try:
            testthis = str(dataread_actual)
        except Exception as e:
            raise ValueError('Invalid chromsome file name passed to program', e)


#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):
    #tmp_input_taxon = ''
    #tmp_input_chromosomenbr = ''
    #tmp_input_debug = ''

    if(len(sys.argv) == 1):
        raise ValueError('taxon is mandatory for this program')
    else:
        tmp_input_taxon = int(sys.argv[1])

    # accession number can be any value, watch positions for next argument though...
    if(len(sys.argv) == 2):
        raise ValueError('Chromosome is mandatory for this program')
    else:
        tmp_input_chromosomenbr = str(sys.argv[2])

    # evaluate print/debug argument
    if(len(sys.argv) == 3):
        raise ValueError('Verbose flags are mandatory for this program')
    else:
        tmp_input_verbose = int(sys.argv[3])
    ##  create a class-chromosome object to work with, then find a string within that
    tmp_cls_chromosome_object = cls_chromosome_object(tmp_input_taxon, tmp_input_chromosomenbr, tmp_input_verbose)
    tmp_cls_chromosome_object.build_chromosome()
