###
# open NCBI upload files in the Gridfs format
# write to collections

from pymongo import MongoClient
import gridfs

client = MongoClient('Ubuntu18Server01')
db = client.Chromosome
fs = gridfs.GridFSBucket(db)

### the following prints an index, not readable data

print('print plain fs: ')
print(fs)

print('\n\nprint plain fs.find(): ')
print(fs.find())

print('\n\n\n')
for dataread in fs.find():
    print('print dataread in loop: ')
    dataread_actual = dataread.read()
    #print(dataread)   # prints an index
    print('The following is the first attempt to make a list of byte data')
    dataread_string = dataread_actual.split(b'\n')
    #print(dataread_string)  # prints the nucleic sequence, but includes \n, not a list-- simply a dump

    ### the following properly breaks out the string (in bytes) into lines
    #print('The following prints the lines as byte data')
    #for dataread_bytelines in dataread_actual.split(b'\n'):
    #    print(dataread_bytelines)

    ### now try converting byte data to string using UTF-8 note: this works very well
    print('The following prints the lines as string date after using ''str''')
    #for dataread_string in str(dataread_actual, encoding='utf-8').split('\n'):
    str(dataread_actual, encoding='utf-8').split('\n')
        #print(dataread_string)
    # now try removing the first element of the list
    dataread_string2 = dataread_string.pop(0)
    print('print dataread_string2 - should be first line of chromosome file')
    print(dataread_string2)
    #print('print dataread_string after pop - should be only nucleotides')
    #print(dataread_string)
