
#import urllib.request
#import shutil
#import requests
import pprint

from pymongo import MongoClient
client = MongoClient()
db = client.chrome
collect = db.mrna

#mcursor = collect.aggregate([{"$project":{"gene_id":1, "accession":1, "_id":0}}])
mcursor = collect.aggregate([ {"$match":{"gene_id":{"$eq":"6003"}}}, {"$unwind":"$exons"}, {"$group": {"_id": {"gene_id":"$gene_id", "exonstart":"$exons.start", "exonend":"$exons.end"}, "total":{"$sum":1}}}, {"$sort":{"exonstart":1, "exonend":1}} ])

print("Start print of individual columns for mcursor")
for record in mcursor:
    print("full record value is: ", record)
    print("try to get value of total: ", record['total'])
    for colvalue in record:
        print("colvalue is: ", colvalue)
        print("colvalue._id is: ", colvalue[0])
        for key in colvalue:
            print("within colvalue, _id: ", key)
    """
    if record[total] > 1:
        print("The gene has at least two mRNA")
    else:
        print("The gene has perhaps one mRNA")
    print(record)
    """
print("Start print of full record mcursor1")
mcursor1 = collect.aggregate([{'$match':{'gene_id': {'$eq':"6003"}}} , {'$unwind':"$exons"}, {'$sort':{ "exons.start":1, "exons.end":1, 'accession':1}}, {'$project':{'_id':0,  'gene_id':1, 'accession':1, 'exons':1 }}])
for record in mcursor1:
    print(record)
