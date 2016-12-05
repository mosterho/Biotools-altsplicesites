
#import urllib.request
#import shutil
#import requests
import pprint

from pymongo import MongoClient
client = MongoClient()
db = client.chrome
collect = db.mrna

prm_gene = "6003"
prm_gene = "862"
#prm_gene = '820'
#prm_gene = '6402'


#mcursor = collect.aggregate([{"$project":{"gene_id":1, "accession":1, "_id":0}}])
#mcursor = collect.aggregate([ {"$match":{"gene_id":{"$eq":"6003"}}}, {"$unwind":"$exons"}, {"$group": {"_id": {"gene_id":"$gene_id", "exonstart":"$exons.start", "exonend":"$exons.end"}, "total":{"$sum":1}}}, {"$sort":{"exonstart":1, "exonend":1}} ])
mcursor = collect.aggregate([ {"$match":{"gene_id":{"$eq": prm_gene}}}, {"$unwind":"$exons"}, {"$group": {"_id": {"gene_id":"$gene_id", "exonstart":"$exons.start", "exonend":"$exons.end"}, "total":{"$sum":1}}}, {"$sort":{"exonstart":1, "exonend":1}} ])

print("Start print of individual columns for mcursor")
for record in mcursor:
    print("full record value is: ", record)
    #print("total count: ", record['total'])

print("\n\nStart print of full record mcursor1")
mcursor1 = collect.aggregate([{'$match':{'gene_id': {'$eq':prm_gene}}} , {'$unwind':"$exons"}, {'$sort':{ "exons.start":1, "exons.end":1, 'accession':1}}, {'$project':{'_id':0,  'gene_id':1, 'accession':1, 'exons':1 }}])
for record in mcursor1:
    print("full record: ",record)
    #print("accession info: ",record['accession'])
    #print("exon info: ",record['exons'])
    #print("exon info start pos: ",record['exons']['start'])

####### begin mainline

prm_gene = int(sys.argv[1])
print ("\n\nArgument passewd in is: ", prm_gene)


