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
import gridfs, re

# use a REGEX "findall" to loop through this single string
# and return a tuple of strings found

x = b'>NC_000001.11ATGTG\nTGATAGTAGATstop\n>NC_000002.11AGTGAT\nGATGTATGTGATAstop\n>PXSHGBJUYGTAS\nLHGSLYUGSLYGLSstop\n>NC_000003.9AGTGTAGT\nAGTGATGstop\n>NC_000005.11ATGTAGTstop'
x_decoded = x.decode()
#x_decoded_sub = re.sub(r'\n', '', x_decoded)
print('x: ', x)
print('x_decoded: ', x_decoded, '\n')
#print('x_decoded_sub: ', x_decoded_sub)

# the following catches everything correctly except the last accession
#pattern = re.compile('>NC_0000.+?(?=>)', re.DOTALL)
pattern = re.compile(r'>NC_0000.+?(?=\n>)', re.DOTALL)
match_object = re.findall(pattern, x_decoded)
#match_object = re.findall(pattern, x_decoded_sub)
for new_list in match_object:
    wrk_filename = new_list[1:10]
    wrk_dataforwrite = new_list.encode()
    print('File name: ', wrk_filename, 'data: ', wrk_dataforwrite)
