
##
##  Main calling program for finding a regex pattern in
##  the GridFS version of NCBI chromosome data
##  Arguments: Taxon (numeric) version of species, pattern to search,
##  chromosome to search (optional), and debugging options.


from pymongo import MongoClient
import sys, re, gridfs
import Build_chromosome_list, Find_regex

class cls_overall_container:
    def __init__(self, arg_taxon, arg_searchpattern, arg_chromosome='', arg_debug=''):
        self.taxon = arg_taxon
        self.searchpattern = arg_searchpattern
        self.chromosome = arg_chromosome
        self.debug = arg_debug

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
        try:
            tmp_rtv_object = self.db.files.find({"filename" : "9600adsfgadfsdsfg"})
            #db.inventory.find( { tags: { $eq: [ "A", "B" ] } } )
            print('This may have worked!!!!! ', tmp_rtv_object)
        except Exception as e:
            raise ValueError('Could not validate taxon passed into this program', e)
        return True

##



#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):
    #tmp_input_organism = 0
    #tmp_input_searchpattern = ''
    #tmp_input_chromosomenbr = ''
    #tmp_input_debug = ''

    if(len(sys.argv) == 1):
        raise ValueError('Taxon/Organism is mandatory for this program')
    else:
        tmp_input_organism = int(sys.argv[1])

    # ...
    if(len(sys.argv) == 2):
        raise ValueError('Search pattern is mandatory for this program')
    else:
        tmp_input_searchpattern = sys.argv[2]
    # ...
    if(len(sys.argv) == 3):
        tmp_input_chromosomenbr = ''
    else:
        tmp_input_chromosomenbr = sys.argv[3]

    # evaluate print/debug argument
    if(len(sys.argv) >= 4):
        if(str(sys.argv[4])[0:2] != '-v' and str(sys.argv[3])[0:3] != '-vv'):
            tmp_input_debug = ''
        else:
            tmp_input_debug = sys.argv[4]

    wrk_container = cls_overall_container(tmp_input_organism, *tmp_input_chromosomenbr, **tmp_input_searchpattern, **tmp_input_debug)
    wrk_valid = wrk_container.fnc_validate_taxon()
