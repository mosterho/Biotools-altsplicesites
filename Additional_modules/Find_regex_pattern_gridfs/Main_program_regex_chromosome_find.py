
##
##  Main calling program for finding a regex pattern in
##  the GridFS version of NCBI chromosome data
##  Arguments: Taxon (numeric) version of species,
##  chromosome to search,
##  pattern to search, and verbose (debugging) options.

import sys, argparse
import Build_chromosome_list, Find_regex

class cls_overall_container:
    def __init__(self, arg_taxon, arg_chromosome, arg_searchpattern, arg_verbose):
        self.taxon = arg_taxon
        # For now, assume arg_chromosome contains only one value
        self.chromosome = []
        for cls_loop in arg_chromosome:
            self.chromosome.append('chromosome' + str(cls_loop))
        self.searchpattern = arg_searchpattern
        self.verbose = arg_verbose
        if(self.verbose in (1,2)):
            print(__name__, ' called from: ', sys.argv[0], '\nTaxon is: ', self.taxon, '\nchromosome(s): ', self.chromosome, '\nSearch Pattern: ', self.searchpattern)

    def fnc_validate_searchpattern(self):
        if(self.searchpattern):
            pass
        else:
            raise ValueError('A search pattern is required')

##

#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):

    ## work with argument parser to build correct parameter/argument values
    wrk_parser = argparse.ArgumentParser(usage="Search chromosome(s) in the GridFS system for a pattern. The arugments accepted include: a single taxon; multiple chromsome numbers (1 2 X Y); a search pattern; verbose output option")
    wrk_parser.add_argument("Taxon", help="the taxon is the numeric ID of the species (e.g., 9606 is homo Sapiens)", type=int)
    wrk_parser.add_argument("-c", "--chromosome", help="the chromosome number of the species. This will accept multiple values (e.g., 1 2 4 X MT)", nargs="*", default='')
    wrk_parser.add_argument("-s", '--SearchPattern', help="the regex search pattern to look for in the chromosome(s)")
    wrk_parser.add_argument("-v", "--verbose", help="Specifiy the level of vebose output, valid values are -v and -vv", action="count", default=0)
    rslt_parser = wrk_parser.parse_args()

    if(rslt_parser.verbose == 2):
        print(__name__, ' ', sys.argv[0], ' ', 'Result of the parser is: ', rslt_parser)

    ## Build class that contains overall info
    wrk_container = cls_overall_container(rslt_parser.Taxon, rslt_parser.chromosome, rslt_parser.SearchPattern, rslt_parser.verbose)
    wrk_valid_searchpattern = wrk_container.fnc_validate_searchpattern()
    if(rslt_parser.verbose == 2):
        print(__name__, ' called from: ', sys.argv[0], ' ', 'Result of the creating container is: ', wrk_container)

    ## Build the chromosome list -- this will contain all info (taxon, some details about chromosome, search pattern)
    wrk_Buildchromosomelist = Build_chromosome_list.cls_all_chromosome(wrk_container.taxon, wrk_container.chromosome, wrk_container.searchpattern,  wrk_container.verbose)
