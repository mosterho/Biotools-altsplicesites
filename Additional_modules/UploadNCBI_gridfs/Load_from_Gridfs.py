###
# open NCBI upload files in the Gridfs format
# write to collections

from pymongo import MongoClient
import gridfs

client = MongoClient('Ubuntu18Server01')
db = client.Chromosome
fs = gridfs.GridFS(db)

## begin printing legiible data
print('\n\n\n')
print('print plain fs.list(): ')
print(fs.list())

print('\n\n\n')
print('print fs.list() within a loop')
for i in fs.list():
    print(i)
