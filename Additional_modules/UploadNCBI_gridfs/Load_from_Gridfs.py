###
# open NCBI upload files in the Gridfs format
# write to collections

from pymongo import MongoClient
import gridfs

client = MongoClient('Ubuntu18Server01')
db = client.Chromosome
fs = gridfs.GridFS(db)

### the following prints an index, not readable data
'''
print('print plain fs: ')
print(fs)

print('\n\nprint plain fs.find(): ')
print(fs.find())

print('\n\n\n')
for dataread in fs.find():
    print('print dataread in loop: ')
    print(dataread)
'''

## begin printing legiible data
print('\n\n\n')
print('print plain fs.list(): ')
print(fs.list())

print('\n\n\n')
print('print fs.list() within a loop')
for i in fs.list():
    print(i)
