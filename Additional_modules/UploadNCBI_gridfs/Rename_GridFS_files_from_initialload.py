
##
## rename files created from the bash shell that loaded the Gridfs
##


from pymongo import MongoClient
import gridfs

client = MongoClient('Ubuntu18Server01')
db = client.Chromosome
fs = gridfs.GridFS(db)
