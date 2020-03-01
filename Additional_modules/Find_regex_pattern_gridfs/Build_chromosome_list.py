
##
## Progam will create a class that contains only
## of a single chromosome (required argument to this program)
## One field/attribute contains a single bytestring list of the nucleotides
## of the one chromosome passed in
## but is still multiline (only the \n is removed)
##
## This behaves in a similar manner to the previous project,
## except that the modules work with the GridFS system.
##
##  arguments:
##    arg_taxon = numeric value for species
##    arg_chromosome = list of multiple full name of a single chromosome such as 'chromosomeX'
##    arg_verbose = numeric equivalent from argparser (-vv = 2)

import sys, chromosome_object, Find_regex

class cls_all_chromosome:
    def __init__(self, arg_taxon, arg_chromosome, arg_searchpattern, arg_verbose):

        ## Build list of self variables for the class, including working list for chromosome object
        self.taxon = arg_taxon
        self.chromosome = arg_chromosome
        self.searchpattern = arg_searchpattern
        self.verbose = arg_verbose
        #working_cls_chromosome_object = []  # can revivie this if appending multiple chromosomes to one object
        if(self.verbose == 2):
            print(__name__, ' called from: ', sys.argv[0], ' ', self.chromosome)

        ## loop though chromosome numbers passed in, append to the working class list
        for i_chromosome in self.chromosome:
            wrk_chromosome = chromosome_object.cls_chromosome_object(self.taxon, i_chromosome, self.verbose)
            wrk_chromosome.build_chromosome()
            ## doing an append to the working list greatly increases memory pressure
            ## perform search on individual wrk_chromosome class objects
            #working_cls_chromosome_object.append(wrk_chromosome)

            # the nucleotides in the class are in a byte list (i.e., multiple lines)
            # convert this to a single byte string
            wrk_str_nucleotide = ''
            tmp_count = 0
            for i in wrk_chromosome.cls_nucleotides:
                tmp_count += 1
                if(self.verbose >= 2 and tmp_count < 6):
                    print(__name__, ' called from: ', sys.argv[0], ' ', 'Nucleotide string: ', '\n', i)
                wrk_str_nucleotide += str(i, encoding='utf-8')
            if(self.verbose >= 2):
                print(__name__, ' called from: ', sys.argv[0], ' ', 'Subset of the full Nucleotide string: ', wrk_str_nucleotide[0:120])
            rtn_matchobject = Find_regex.fnc_search(self.searchpattern, wrk_str_nucleotide, self.verbose)

            if(self.verbose >= 1):
                print(__name__, ' called from: ', sys.argv[0], ' ', 'a subset of the returned match object is: ', rtn_matchobject[0:5])
                print(__name__, ' called from: ', sys.argv[0], ' ', 'Class object for ', i_chromosome, ' complete')
        #if(self.verbose == 2):
            #print(__name__, ' called from: ', sys.argv[0], ' ', 'Full working class chromosome object (i.e. all chromosomes): ', working_cls_chromosome_object)


#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):

    if(len(sys.argv) == 1):
        raise ValueError('taxon is mandatory for this program')
    else:
        tmp_input_taxon = int(sys.argv[1])

    # accession number can be any value,
    if(len(sys.argv) == 2):
        raise ValueError('Chromosome is mandatory for this program')
    else:
        tmp_input_chromosomenbr = [sys.argv[2]]

    # search pattern must be a regex pattern,
    if(len(sys.argv) == 3):
        raise ValueError('regex search pattern  is mandatory for this program')
    else:
        tmp_input_searchpattern = str([sys.argv[3]])

    # evaluate print/debug argument
    if(len(sys.argv) == 4):
        raise ValueError('Verbose flags are mandatory for this program')
    else:
        tmp_input_verbose = int(sys.argv[4])

    ##  create a class-chromosome object to work with, then find a string within that
    tmp_cls_chromosome_object = cls_all_chromosome(tmp_input_taxon, tmp_input_chromosomenbr, tmp_input_searchpattern,  tmp_input_verbose)
