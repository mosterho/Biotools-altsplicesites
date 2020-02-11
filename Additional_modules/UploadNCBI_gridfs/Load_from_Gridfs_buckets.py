###
# open NCBI upload files in the Gridfs format
# write to collections

from pymongo import MongoClient
import gridfs, sys

client = MongoClient('Ubuntu18Server01')
db = client.Chromosome
fs = gridfs.GridFSBucket(db)

### the following prints an index, not readable data
print('print plain fs: ')
print(fs)
print('print plain fs.find(): ')
print(fs.find())

print('\n\n\nStart FOR loop of fs.find() into dataread variable')
for dataread in fs.find():
    print('\n\n***NEW chromosome - Load byte data into variable for each file (chromosome), print dataread in loop: ')
    dataread_actual = dataread.read()
    #print(dataread)   # prints an index
    print('Create a list of byte data from the file/bucket, SPLIT off newline')
    dataread_actual_bytelist = dataread_actual.split(b'\n')
    print('use FOR loop to print the first 5 lines of the list')
    for i in range(5):
        print(dataread_actual_bytelist[i])

    ### now try converting byte data to string using UTF-8 note: this works very well
    print('Use ''str'' to convert byte data to "regular" list and SPLIT off newline')
    dataread_actual_list = str(dataread_actual, encoding='utf-8').split('\n')
    print('use FOR loop to print the first 5 lines of the list')
    for i in range(5):
        print(dataread_actual_list[i])
    # now try removing the first element of the list
    print('Use POP to remove the first line (this contains the >gi| and description of the file)')
    dataread_actual_firstline = dataread_actual_list.pop(0)
    print('print dataread_actual_firstline - should be first line of chromosome file')
    print(dataread_actual_firstline)
    print('print dataread_actual_list after pop - should be only nucleotides')
    for i in range(5):
        print(dataread_actual_list[i])
    #
    # call retrieve_pattern with "dataread_actual_list"



#-------------------------------------------------------------------------------
#### begin mainline

###  this can be used as either a module or standalone program,
###  depending on where/how it's called

if (__name__ == "__main__"):
    tmp_input_searchpattern = ''
    tmp_input_organism = ''
    tmp_input_accessionnbr = ''
    tmp_input_print = ''

    if(len(sys.argv) == 1):
        raise ValueError('Search pattern is mandatory for the first argument for this program')
    else:
        tmp_input_searchpattern = str(sys.argv[1])

    if(len(sys.argv) == 2):
        raise ValueError('Organism is mandatory for this program')
    else:
        tmp_input_organism = str(sys.argv[2])

    # accession number can be any value, watch positions for next argument though...
    if(len(sys.argv) >= 4):
        tmp_input_accessionnbr = str(sys.argv[3])

    # if second (print/debug) argument exists, but is not 'Y', just default to blank/empty string
    if(len(sys.argv) == 5):
        if(sys.argv[4] != 'Y'):
            tmp_input_print = ''
        else:
            tmp_input_print = sys.argv[4]

    get_pattern(tmp_input_searchpattern, tmp_input_organism, tmp_input_accessionnbr, tmp_input_print)
