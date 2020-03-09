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

client = MongoClient('Ubuntu18Server01')
db = client.Genome
#fs = gridfs.GridFS(db)  # for writing to a new file
fsbucket = gridfs.GridFSBucket(db)  # for reading the existing Genome file

print('Use loop example to print rows of data')
grid_out = fsbucket.open_download_stream_by_name("9606_Genome_protein")
# begin loop reading through genome colleciton
wrk_tag = False
wrk_filename = ''
wrk_data = ''
for x in grid_out:
    another_loop = x.split(b'\n')  # split creates a list
    for new_list in another_loop:
        if(new_list[0:3] == b'>NC'):
            wrk_tag = True
            wrk_filename = str(new_list)
            print(new_list[:100])
            #wrk_data += str(new_list, encoding='utf-8')
            wrk_data += new_list.decode()
        elif(new_list[0:1] != b'>' and wrk_tag):
            wrk_data += new_list.decode()
        elif(new_list[0:3] != b'>NC' and new_list[0:1] == b'>' and wrk_tag):
            #fs.put(wrk_data.encode(), filename = wrk_filename)
            fsbucket.upload_from_stream(wrk_filename.decode(), wrk_data.encode())
            wrk_tag = False
            wrk_data = ''
    # end of all data reads, write last buffer setup from loop above
    fsbucket.upload_from_stream(wrk_filename.decode(), wrk_data.encode())
