
##
##  Main calling program for finding a regex pattern in
##  the GridFS version of NCBI chromosome data
##  Arguments: Taxon (numeric) version of species, pattern to search,
##  chromosome to search (optional), and debugging options.


from pymongo import MongoClient
import sys, re, gridfs, argparse
import Build_chromosome_list, Find_regex

class cls_overall_container:
    def __init__(self, arg_taxon, arg_chromosome, arg_searchpattern, arg_verbose):
        self.taxon = arg_taxon
        # For now, assume chromosome contains only one value
        for cls_loop in arg_chromosome:
            self.chromosome = 'chromosome' + str(cls_loop)
        self.searchpattern = arg_searchpattern
        self.verbose = arg_verbose

        client = MongoClient('Ubuntu18Server01')
        self.db = client.Chromosome
        self.fs       = gridfs.GridFS(self.db)
        self.fsbucket = gridfs.GridFSBucket(self.db)

    def fnc_retrieve_chromosome(self):
        pass
    def fnc_chromosome(self):
        pass
    def fnc_find_pattern(self):
        pass
    def fnc_validate_taxon(self):
        ##
        ## build a serch string for $regex
        tmp_search = '/^' + str(self.taxon) + '_' + self.chromosome + '/'
        #for dataread in self.fsbucket.find({"filename" : {"$regex" : "$$tmp_search"}}):
        for dataread in self.fsbucket.find({"filename" : str(self.taxon) + '_' + self.chromosome}):
            print('This may have worked!!!!! ', str(dataread.read()[0:79]))
        try:
            teststring = str(dataread)
        except Exception as e:
            print(self.taxon, ' ', self.chromosome)
            raise ValueError('Could not validate taxon passed into this program', e)
        return True

##



#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):

    wrk_parser = argparse.ArgumentParser()
    wrk_parser.add_argument("Taxon", help="the taxon is the numeric ID of the species e.g., 9606 is homo Sapiens", type=int)
    wrk_parser.add_argument("-c", "--chromosome", help="the chromosome number of the species. This will accept multiple values e.g., 1 2 4 X MT", nargs="*", default='')
    wrk_parser.add_argument("-s", '--SearchPattern', help="the regex search pattern to look for in the chromosome(s)")
    wrk_parser.add_argument("-v", "--verbose", help="Specifiy the level of vebose output, valid values are -v and -vv", action="count", default=0)
    rslt_parser = wrk_parser.parse_args()

    wrk_container = cls_overall_container(rslt_parser.Taxon, rslt_parser.chromosome, rslt_parser.SearchPattern, rslt_parser.verbose)
    wrk_valid = wrk_container.fnc_validate_taxon()
