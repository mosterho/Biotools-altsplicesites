
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

from pymongo import MongoClient
import gridfs, sys

class cls_chromosome_object:
    def __init__(self, arg_organism, arg_chromosome, arg_debug):
        ### arg_organism contains the number of the Organism
        ### arg_chromosome contains the chromosme number (e.g., chromome1, chromsome12, etc.)
        self.cls_organism = arg_organism
        self.cls_chromosome = arg_chromosome
        self.cls_debug = arg_debug
        self.cls_nucleotides = ''

    def build_chromosome(self, arg_chromosome):
        ### Use the class cls_seq to create the bytelist of a chromsome, SPLIT off newline characters
        ### and return a list bytelist of nucleotides
        client = MongoClient('Ubuntu18Server01')
        db = client.Chromosome
        fs = gridfs.GridFSBucket(db)

        ### the following prints an index, not readable data
        if(self.cls_debug == '-v' or self.cls_debug == '-vv'):
            #print('print plain fs: ')
            #print(fs)
            print('print ID for bucket for fs.find({"filename":' + self.cls_chromosome + '}): ')
            print(fs.find({"filename":self.cls_chromosome}))
        for dataread in fs.find({"filename":self.cls_chromosome}):
            #print('\n\n***NEW chromosome - Load byte data into variable for each file (chromosome), print dataread in loop: ')
            dataread_actual = dataread.read()
            #print('Create a list of byte data from the file/bucket, SPLIT off newline')
            dataread_actual_bytelist = dataread_actual.split(b'\n')
            if(self.cls_debug == '-vv'):
                print('\nuse FOR loop to print the first 5 lines of the list')
                for i in range(5):
                    print(dataread_actual_bytelist[i])
            #Use POP to remove the first line (this contains the >gi|, description of the file, etc.)
            dataread_actual_firstline = dataread_actual_bytelist.pop(0)
            if(self.cls_debug == '-vv'):
                print('\nprint dataread_actual_firstline - should be first line of chromosome file')
                print(dataread_actual_firstline)
                print('print dataread_actual_list after pop - should be only nucleotides')
                for i in range(5):
                    print(dataread_actual_bytelist[i])
        try:
            testthis = str(dataread_actual)
        except:
            raise ValueError('Invalid chromsome file name passed to program')
            return

        return(dataread_actual_bytelist)

#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):
    tmp_input_organism = ''
    tmp_input_chromosomenbr = ''
    tmp_input_debug = ''

    if(len(sys.argv) == 1):
        raise ValueError('Organism is mandatory for this program')
    else:
        tmp_input_organism = int(sys.argv[1])

    # accession number can be any value, watch positions for next argument though...
    if(len(sys.argv) == 2):
        raise ValueError('Chromosome is mandatory for this program')
    else:
        tmp_input_chromosomenbr = str(sys.argv[2])

    # evaluate print/debug argument
    if(len(sys.argv) == 4):
        if(str(sys.argv[3])[0:2] != '-v' and str(sys.argv[3])[0:3] != '-vv'):
            tmp_input_debug = ''
        else:
            tmp_input_debug = sys.argv[3]
    tmp_cls_chromosome_object = cls_chromosome_object(tmp_input_organism, tmp_input_chromosomenbr, tmp_input_debug)
    rtn_chromosome_list = tmp_cls_chromosome_object.build_chromosome(tmp_input_chromosomenbr)
