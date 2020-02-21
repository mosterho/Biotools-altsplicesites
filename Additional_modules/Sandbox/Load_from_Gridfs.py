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


print('\n\n\n')
print('Try dbcollection to find one file  ')
#print(fs.exists({"filename" : /^9606_chromosome10.*/i}))
#print(fs.exists({ /^9606_chromosome10.*/i}))
print(fs.exists({"filename" : "9606_chromosome10"}))
print('db.fs.files.find({"filename":"9606_chromosome10"})', db.fs.files.find({"filename":"9606_chromosome10"}))
print('db.fs.files.find({"filename":"9609"})', db.fs.files.find({"filename":"9609"}))


#print('Use loop example of find() on gridfs python section') This prints a lot of data
#for grid_out in fs.find_one({"filename": "9606_chromosome1"}):
#    print('value of "data" within loop', grid_out)
