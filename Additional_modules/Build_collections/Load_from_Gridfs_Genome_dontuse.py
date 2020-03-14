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
from datetime import datetime, timedelta
import gridfs

client = MongoClient('mongodb')
db = client.Genome
fs_forwrite = gridfs.GridFS(db)  # for writing to a new file
fs          = gridfs.GridFSBucket(db)

#grid_out = fs_datafind.read()
# begin loop reading through genome colleciton
wrk_tag = False
wrk_filename = ''
wrk_data = ''
print('Starting: ', datetime.now())

for fs_datafind in fs.find({"filename":"9606_Genome"}):
    x = fs_datafind.read()
    start_time = datetime.now()
    print('x from read() is: ', x[:100], 'at: ', start_time)
    another_loop = x.split(b'\n')  # split creates a list
    for new_list in another_loop:
        # if wrk_tag is set and b'>' (any new accession) is encountered,
        # write the accession data and reset wrk_tag'
        if(wrk_tag and new_list[0:1] == b'>'):
            wrk_dataforwrite = wrk_data.encode()
            fs_forwrite.put(wrk_dataforwrite, disable_md5 = True, filename=wrk_filename)
            wrk_tag = False
            wrk_data = ''
        # check for new accession number encountered, set basic file data
        if(new_list[0:3] == b'>NC'):
            if(not wrk_tag):
                wrk_tag = True
                wrk_filename = str(new_list[1:10], encoding='utf-8')
                print('New accession number starting: ', wrk_filename, ' ', new_list[:100],  'at: ', datetime.now())
            wrk_data += str(new_list)
            #wrk_data += new_list.decode()
        # if not an accession number, but could be data, concatenate to wrk_data
        elif(new_list[0:1] != b'>' and wrk_tag):
            wrk_data += new_list.decode()
    # end of all data reads, write last buffer setup from loop above
    if(wrk_tag):
        wrk_tag = False
        #fsbucket.upload_from_stream(wrk_filename.decode(), wrk_data.encode())
        wrk_dataforwrite = wrk_data.encode()
        fs_forwrite.put(wrk_dataforwrite, disable_md5 = True, filename=wrk_filename)
        end_time = datetime.now()
        print('Finished at: ', end_time, '   total time: ', end_time-start_time)
