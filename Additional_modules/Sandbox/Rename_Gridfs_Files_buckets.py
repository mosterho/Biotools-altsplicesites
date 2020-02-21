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
    #dataread_actual = dataread.read()
    dataread_actual = dataread.find()   # find isn't a valid method
    #print(dataread_actual)
    #file_id = fs.upload_from_stream("test_file", "data I want to store!")
    #fs.rename(file_id, "new_test_name")
