
##
## Progam will create a chromosome class and find the nucleotides
## of a single chromosome (required argument to this program)
## and return a single bytestring list of the nucleotides of the
## one chromosome passed in
## but is still multiline (only the \n is removed)
##
## This behaves in a similar manner to the previous project,
## except that the modules work with the GridFS system.
##
##  arguments:
##    arg_taxon = numeric value for species
##    arg_chromosome = list of multiple full name of a single chromosome such as 'chromosomeX'
##    arg_verbose = numeric equivalent from argparser (-vv = 2)


#from pymongo import MongoClient
import sys, chromosome_object

class cls_all_chromosome:
    def __init__(self, arg_taxon, arg_chromosome, arg_verbose):

        self.taxon = arg_taxon
        self.chromosome = arg_chromosome
        self.verbose = arg_verbose
        working_cls_chromosome_object = []
        if(self.verbose == 2):
            print(__name__, ' called from: ', sys.argv[0], ' ', self.chromosome)
        for i_chromosome in self.chromosome:
            wrk_chromosome = chromosome_object.cls_chromosome_object(self.taxon, i_chromosome, self.verbose)
            wrk_chromosome.build_chromosome()
            working_cls_chromosome_object.append(wrk_chromosome)
            if(self.verbose == 1):
                print(__name__, ' called from: ', sys.argv[0], ' ', 'Class object for ', i_chromosome, ' complete')
        if(self.verbose == 2):
            print(__name__, ' called from: ', sys.argv[0], ' ', 'Full working class chromosome object (i.e. all chromosomes): ', working_cls_chromosome_object)


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
        tmp_input_chromosomenbr = [sys.argv[2]]

    # evaluate print/debug argument
    if(len(sys.argv) == 3):
        raise ValueError('Verbose flags are mandatory for this program')
    else:
        tmp_input_verbose = int(sys.argv[3])

    ##  create a class-chromosome object to work with, then find a string within that
    tmp_cls_chromosome_object = cls_all_chromosome(tmp_input_taxon, tmp_input_chromosomenbr, tmp_input_verbose)

else:
    pass
#if(self.verbose == 2):
    #print('printing "Body" info for: ', sys.argv[0], ' ', __name__)
    #print('Type of object passedin: ', type(sys.argv[2]))
