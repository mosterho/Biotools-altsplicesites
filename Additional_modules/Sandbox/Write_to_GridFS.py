###
# open NCBI upload files in the Gridfs format
# write to collections
# This will create various chromosome collections in the
# Genome database. Read the "9606_Genome" collection created by
# the BASH script, write each chromosome as a collection
# while looping through the fsbucket, catch each instance of ">NC"
# until the next ">" is read (this will be the changed assemblies)
# then pick up again at the next ">NC" that is read.

from pymongo import MongoClient
import gridfs

client = MongoClient('mongodb')
db = client.Genome
fs_forwrite = gridfs.GridFS(db)  # for writing to a new file
fs          = gridfs.GridFSBucket(db)

# build wrk_data similar to a loop decoding data read from a file.
wrk_data_temp = ''
wrk_filename = 'begin_test_only'
wrk_data = b'>begin basic write'
wrk_data_temp += str(wrk_data, encoding='utf-8')
wrk_data = b'>second line'
wrk_data_temp += str(wrk_data, encoding='utf-8')
wrk_data = b'\n>third line but with \n at the beginning'
wrk_data_temp += wrk_data.decode()
wrk_data_write = wrk_data_temp.encode()
fs_forwrite.put(wrk_data_write, disable_md5 = True, filename=wrk_filename)
print('The test write may have worked', '\n\n')

wrk_filename = 'begin_test_only2'
wrk_data2 = wrk_data_temp.encode()
fs_forwrite.put(wrk_data2, disable_md5 = True, filename=wrk_filename)
print('The test write may have worked', '\n\n')
